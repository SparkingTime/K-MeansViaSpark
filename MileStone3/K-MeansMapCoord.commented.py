'''
This script Calculate Geomedian by averaging Lon/Lat directly
Add is implemented through numpy array
'''
from __future__ import print_function

import sys
import csv
import numpy as np
from pyspark import SparkContext
from haversine import haversine as hv

#retrieve latitude and longitude of every record
def generateVector(line):
    result = []
    linewords = line.split(',')
    result.append(float(linewords[0]))
    result.append(float(linewords[1]))
    return np.array(result)

#retrieve index of the cluster cernter that is closest to p in greate circle distance
def closestCenterHaversine(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = hv(p, centers[i])
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex


#retrieve index of the cluster cernter that is closest to p in Euclidean distance
def closestCenterEuclidean(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = np.sum((p - centers[i])**2)
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex

#retrieve map output in greate circle distance(key: index of the closest center, value: (point, 1, point in list format))
def mapHaversine(p):
    return (closestCenterHaversine(p, kPoints), (p, 1, p.tolist()))

#retrieve map output in Euclidean distance(key: index of the closest center, value: (point, 1, point in list format))
def mapEuclidean(p):
    return (closestCenterEuclidean(p, kPoints), (p, 1, p.tolist()))

#reduce method 
def testMethod(p1v, p2v):
    return (p1v[0] + p2v[0], p1v[1] + p2v[1],p1v[-1] + p2v[-1])


if __name__ == "__main__":

    # input checking
    if len(sys.argv) != 6:
        print("Usage: kmeans <file> <k> <convergeDist> <DistanceMethod> <dir> ",
              file=sys.stderr)
        exit(-1)

    #input retrieve
    sc = SparkContext("local[5]",appName="PythonKMeans")
    lines = sc.textFile(sys.argv[1])
    data = lines.map(generateVector).cache()
    K = int(sys.argv[2])
    convergeDist = float(sys.argv[3])
    DistanceMethod = sys.argv[4]
    dirName = sys.argv[5]
    
    #choose k initial cluster centers at random
    kPoints = data.takeSample(False, K, 1)
    it = 0
    tempDist = float('inf')
    global_min = float('inf')
    while tempDist > convergeDist and it < 1:
        #states checking 
        print("<-@@@@@@@@@@@@@@@@@@@@@@-----------------------------------------------------" + "Distance: "+ str(tempDist) + " on iteration "+ str(it) +"------------------------------------------------------@@@@@@@@@@@@@@@@@@@@@@->")
        #mapper output
        if(DistanceMethod == "Euclidean"):
            closest = data.map(mapEuclidean)
        elif(DistanceMethod == "GreateCircle"):
            closest = data.map(mapHaversine)
        else:
            print("WTF DID YOU SAY? MAN, GreateCircle/Euclidean please")
            exit(-1)
        #reducer output
        pointStats = closest.reduceByKey(testMethod,5) 
        #pointStats = closest.reduceByKey(testMethod) 
        #new cluster centers
        newPoints = pointStats.map(
            lambda st: (st[0], st[1][0] / st[1][1])).collect()
        if(DistanceMethod == "Euclidean"):
            tempDist = sum(np.sum((kPoints[iK] - p) ** 2)
                           for (iK, p) in newPoints)
        else:
            tempDist = sum(hv(kPoints[iK], p) for (iK, p) in newPoints)
        for (iK, p) in newPoints:
            kPoints[iK] = p
        #update temperary distance 
        if tempDist < global_min:
    	    pointsInfo = pointStats
            global_min = tempDist
        it = it + 1

    pointsInfo = pointsInfo.collect()
    outputFilePath ="./step3.Output/" + dirName+ "/cluster_centers.csv"
    result = []
    for ele in:
        result.append(ele.tolist())
      
    with open(outputFilePath, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(result)

    counter = 0
    # Iterate through kPoints  and make kcenters
    for file in pointsInfo:
        numofpoints = file[1][1]
        centerIndex = file[0]
        result = []
        result.append(kPoints[centerIndex].tolist())
        if numofpoints == 1:
            pass
        else:
            flattenedpoints = file[1][2]
            for i in range(0, len(flattenedpoints), 2):
                result.append([flattenedpoints[i], flattenedpoints[i + 1]])
        outputFilePath ="./step3.Output/" + dirName+ "/cluster_" + str(counter) + ".csv"
        with open(outputFilePath, "wb") as f:
            writer = csv.writer(f)
            writer.writerows(result)
        counter = counter + 1
    sc.stop()
 
