'''
This script Calculate Geomedian by averaging Lon/Lat directly
Add is implemented through numpy array
'''
from __future__ import print_function

import sys

import numpy as np
from pyspark import SparkContext
from haversine import haversine as hv

def generateVector(line):
    result = []
    linewords = line.split(' ')
    result.append(float(linewords[0]))
    result.append(float(linewords[1]))
    return np.array(result)


def closestCenterHaversine(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = hv(p,centers[i])
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex


def closestCenterEuclidean(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = np.sum( (p-centers[i])**2 )
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex



def mapHaversine(p):
    return (closestCenterHaversine(p, kPoints), (p, 1))
def mapEuclidean(p):
    return (closestCenterEuclidean(p, kPoints), (p, 1))



if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: kmeans <file> <k> <convergeDist> <DistanceMethod>", file=sys.stderr)
        exit(-1)

    print("""WARN: This is a naive implementation of KMeans Clustering and is given
       as an example! Please refer to examples/src/main/python/mllib/kmeans.py for an example on
       how to use MLlib's KMeans implementation.""", file=sys.stderr)

    sc = SparkContext(appName="PythonKMeans")
    lines = sc.textFile(sys.argv[1])
    data = lines.map(generateVector).cache()
    K = int(sys.argv[2])
    convergeDist = float(sys.argv[3])
    DistanceMethod = sys.argv[4]

    kPoints = data.takeSample(False, K, 1)
    tempDist = 1.0

    while tempDist > convergeDist:
        if(DistanceMethod=="Euclidean"):
            closest = data.map(mapEuclidean)
        elif(DistanceMethod=="GreateCircle"):
            closest = data.map(mapHaversine)
        else:
            print("WTF DID YOU SAY? MAN, GreateCircle/Euclidean please")
            exit(-1)


        pointStats = closest.reduceByKey(
            lambda p1_c1, p2_c2: (p1_c1[0] + p2_c2[0], p1_c1[1] + p2_c2[1]))
        newPoints = pointStats.map(
            lambda st: (st[0], st[1][0] / st[1][1])).collect()

        if(DistanceMethod=="Euclidean"):
            tempDist = sum(np.sum((kPoints[iK] - p) ** 2) for (iK, p) in newPoints)
        else:
            tempDist = sum(  hv(kPoints[iK],p) for (iK,p) in newPoints )

        for (iK, p) in newPoints:
            kPoints[iK] = p

    print("Final centers: " + str(kPoints))
    print("points Stats: " + str(pointStats.collect() ))
    sc.stop()
