import array as arr
from numpy import *

from SMetric import SMetricQualityIndicator
from AnalyticHierarchyProcess import ahp, pairWiseComparison, consistencyCheck
from AHP_Final_Rank_Figure import plot
from PROMETHEEPreferenceFunctions import uni_cal
from PROMETHEEFinalRankFigure import plot as plotpromethee
from PROMETHEEII import promethee

def main():
    #---------------------------------------------------------------------------
    # MILLER-TUCKER-ZEMLIN

    pointsMIPGAP0Dot05 = [
        [1560,34],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,33],
        [1620,32],
        [1620,32],
        [1620,33],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32],
        [1680,32]
    ]
    
    SMetricQualityIndicator(pointsMIPGAP0Dot05, "MDVRPTW")

    # pointsMIPGAP0Dot05 = [
    #     [24.6, 1239  ,  1], 
    #     [23.2, 1228.3,  2], 
    #     [21.1, 1262.8,  3], 
    #     [19.4, 1286.5,  2], 
    #     [18.9, 1297.5,  1], 
    #     [18.3, 1324.2,  3], 
    #     [17.5, 1379.5,  2], 
    #     [17.1, 1408.5,  3], 
    #     [16.9, 1427.7,  3], 
    #     [16.7, 1460.2,  2],
    #     [17	 , 1620.2,  1]
    # ]

    # numberOfAlternatives = 11

    # numberOfCriteria = 3

    # fobjmintime = arr.array('d', [])
    # fobjmindist = arr.array('d', [])
    # likeness = arr.array('d', [])
    # for point in pointsMIPGAP0Dot05:
    #     fobjmintime.append(point[0])
    #     fobjmindist.append(point[1])
    #     likeness.append(point[2])

    # PCM1 = pairWiseComparison(fobjmintime, 11, 5)
    # consistencyCheck(PCM1, numberOfAlternatives, numberOfCriteria)
    # PCM2 = pairWiseComparison(fobjmindist, 11, 300)
    # consistencyCheck(PCM2, numberOfAlternatives, numberOfCriteria)
    # PCM3 = pairWiseComparison(likeness, 11, 1)
    # consistencyCheck(PCM3, numberOfAlternatives, numberOfCriteria)

    # allPCM = vstack((PCM1, PCM2, PCM3))

    # PCcriteria = array([[1,   1,   5], 
    #                     [1,   1,   5],
    #                     [1/5, 1/5, 1]])

    # scores = ahp(allPCM, PCcriteria, numberOfAlternatives, numberOfCriteria, 1)

    # print("Global priorities = ", scores)

    # plot(around(scores, 3), "AHP - MTZ")
    
    # #PROMETHEE
    # # preference parameters of all criteria array
    # p = array([
    #     [5,  150,  1], 
    #     [10, 300,  2]])

    # # criteria min (0) or max (1) optimization array
    # c = ([0, 0, 1])

    # # preference function array
    # d = (['li', 'li', 'li'])

    # # weights of criteria
    # w = array([0.5, 0.4, 0.1])

    # final_net_flows = promethee(array(pointsMIPGAP0Dot05), p, c, d, w)
    # print("Global preference flows = ", final_net_flows)
    # plotpromethee(final_net_flows, "PROMETHEE II - MTZ")

if __name__ == '__main__':
    main()
