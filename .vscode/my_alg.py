from pygmo import *
from pygmo.util import *
import random

class my_hv_moo_alg(algorithm.base):
   """
   A custom steady-state algorithm, based on the hypervolume computation.
   """

   def __init__(self, gen = 10, p_m = 0.02):
      """
      Constructs an instance of the algorithm.

      USAGE: my_hv_moo_alg(gen=10, p_m=0.02)

      NOTE: Evolves the population using the least contributor feature.

      * gen: number of generations
      * p_m: probability of mutation
      """
      #We start calling the base constructor
      super(my_hv_moo_alg,self).__init__()
      # Store the number of generations
      self.__gen = gen
      self.__p_m = p_m

   # Performs a very simple crossover step
   def cross(self, ind1, ind2):
      x1 = ind1.cur_x
      x2 = ind2.cur_x
      return tuple(random.choice((x1[i], x2[i],)) for i in xrange(len(x1)))

   # Gaussian mutation
   def mutate(self, x, lb, ub):

      # Implementation of the Gaussian operator
      def _g_op(i):
         return min(max(random.gauss(x[i], (ub[i]-lb[i]) * 0.1), lb[i]), ub[i])

      # Condition for the mutation to happen
      def _rnd_mut():
         return random.random() < self.__p_m

      return tuple(_g_op(i) if _rnd_mut() else x[i] for i in xrange(len(x)))

   # Evolve method
   def evolve(self, pop):
      #If the population is empty (i.e. no individuals) nothing happens
      if len(pop) == 0:
           return pop

      #The algorithm now starts manipulating the population
      prob = pop.problem
      lb, ub = prob.lb, prob.ub
      for s in range(self.__gen):
         # Initiate new individual by a crossover of two random individuals
         idx1 = random.randint(0, len(pop) - 1)
         idx2 = (idx1 + random.randint(0, len(pop) - 2)) % len(pop)
         ind1 = pop[idx1]
         ind2 = pop[idx2]

         new_x = self.mutate(self.cross(ind1, ind2), lb, ub)
         #new_x = self.cross(ind1, ind2)
         pop.push_back(new_x)

         # Remove the least contributor
         hv = hypervolume(pop)
         ref_point = hv.get_nadir_point(1.0)
         lc_idx = hv.least_contributor(ref_point)

         pop.erase(lc_idx)
      return pop

   def get_name(self):
         return "Custom HV-based MOO"

def main():
   prob = problem.dtlz(2)
   alg = my_hv_moo_alg(gen = 100, p_m=0.02)
   pop = population(prob, 100)
   # Establish a constant reference point, so the increase is noticed
   ref_point = (3000,) * 3
   for _ in xrange(100):
      pop = alg.evolve(pop)
      print ("P-Distance: %.5f, Hypervolume: %.5f" % (prob.p_distance(pop), hypervolume(pop).compute(ref_point)))
   prob.plot(pop)

if __name__ == "__main__":
   main()