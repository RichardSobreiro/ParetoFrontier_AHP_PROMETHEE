from pygmo import hypervolume
import pygmo as pg
import numpy as np
import matplotlib.pyplot as plt
import array as arr

def SMetricQualityIndicator(points, title):

    fobjmintime = arr.array('d', [])
    fobjmindist = arr.array('d', [])

    for point in points:
        fobjmintime.append(point[0])
        fobjmindist.append(point[1])

    hv = hypervolume(points)
    ref_point = np.array([1700, 35])
    sMetric = hv.compute(ref_point)
    plt.annotate('Nadir', (ref_point[0], ref_point[1]), color='black')

    n = len(fobjmintime)
    colors = np.random.rand(n)
    plt.scatter(fobjmintime, fobjmindist, c=colors, alpha=0.5)
    plt.xlabel('Lucro')
    plt.ylabel('Viagens não atendidas')
    plt.legend(loc="lower left")

    plt.title(title + ' - S-metric: ' + str(round(sMetric, 2)))

    plt.show()
