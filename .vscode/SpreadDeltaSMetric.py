from pygmo import hypervolume
import pygmo as pg
import numpy as np
import matplotlib.pyplot as plt
import array as arr

def SpreadDeltaSMetricQualityIndicator(points, title):
    extremeFobj1 = np.array((points[0][0], points[0][1]))
    extremeParetoFront1 = np.array((points[1][0], points[1][1]))
    df = np.linalg.norm(extremeFobj1 - extremeParetoFront1)

    extremeFobj2 = np.array((points[-1][0], points[-1][1]))
    extremeParetoFront2 = np.array((points[-2][0], points[-2][1]))
    dl = np.linalg.norm(extremeFobj2 - extremeParetoFront2)

    fobjmintime = arr.array('d', [])
    fobjmindist = arr.array('d', [])

    for point in points:
        fobjmintime.append(point[0])
        fobjmindist.append(point[1])

    n = len(fobjmintime)
    norms = np.array([])
    for index in range(2, n-1):
        d1 = np.array((points[index - 1][0], points[index - 1][1]))
        d2 = np.array((points[index][0], points[index][1]))
        norms = np.append(norms, np.linalg.norm(d2 - d1))

    dAverage = sum(norms) / len(norms)

    sumNorms = 0
    for norm in norms:
        r = norm - dAverage
        if r < 0:
            r *= -1
        sumNorms += r

    DELTA = (df + dl + sumNorms) / (df + dl + (len(norms) * dAverage))

    hv = hypervolume(points)
    ref_point = np.array([1700, 35])#
    #ref_point = pg.nadir(points)
    sMetric = hv.compute(ref_point)
    plt.annotate('Nadir', (ref_point[0], ref_point[1]), color='black')

    colors = np.random.rand(n)
    plt.scatter(fobjmintime, fobjmindist, c=colors, alpha=0.5)
    plt.plot(
        [points[0][0], points[1][0]], 
        [points[0][1], points[1][1]], 
        lw=3, 
        color='black', 
        clip_on=False, 
        label="dl")
    plt.plot(
        [points[-1][0], points[-2][0]], 
        [points[-1][1], points[-2][1]], 
        lw=3, 
        color='red', 
        clip_on=False, 
        label="df")
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.legend(loc="lower left")

    plt.title(title + ' - DELTA: '+ str(round(DELTA,3)) + ' | S-metric: ' + str(round(sMetric, 2)))

    plt.show()
