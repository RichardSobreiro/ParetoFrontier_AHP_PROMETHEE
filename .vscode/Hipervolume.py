from pygmo import hypervolume
import pygmo as pg
import numpy as np
import matplotlib.pyplot as plt
import array as arr

points = [
    [27, 1298.4], 
    [24.8, 1303.2], 
    [22.1, 1313.3], 
    [20.5, 1320.3], 
    [19.5, 1341.8], 
    [19.3, 1379.6], 
    [18.3, 1449.4], 
    [17.8, 1480.8], 
    [17.7, 1473.3], 
    [18, 1549],
    [17.4, 1652.5]
]

fobjmintime = arr.array('d', [])
fobjmindist = arr.array('d', [])

for point in points:
    fobjmintime.append(point[0])
    fobjmindist.append(point[1])

n = len(fobjmintime)

colors = np.random.rand(n)
area = (30 * np.random.rand(n))**2  # 0 to 15 point radii

plt.scatter(fobjmintime, fobjmindist, c=colors, alpha=0.5)

hv = hypervolume(points)
ref_point = pg.nadir(points)
print(hv.compute(ref_point))

plt.annotate('Nadir', (ref_point[0], ref_point[1]), color='black')
plt.show()
