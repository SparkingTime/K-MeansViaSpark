import numpy as np
import csv
a = [(0, (np.array([ 5.,  6.]), 1)), (1, (np.array([ 4.,  6.]), 2, [1.0, 2.0, 3.0, 4.0]))]
kpoints = [np.array([ 5.,  6.]), np.array([ 2.,  3.])]

counter = 0
for file in a:
    numofpoints = file[1][1]
    centerIndex = file[0]
    result = []
    result.append(kpoints[centerIndex].tolist())
    if numofpoints ==1:
        pass
    else:
        flattenedpoints = file[1][2]
        for i in range(0,len(flattenedpoints),2):
            result.append([flattenedpoints[i],flattenedpoints[i+1] ])
    outputFilePath = "cluster_"+str(counter)+".csv"
    with open(outputFilePath, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(result)
    counter = counter +1
