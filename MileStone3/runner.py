#!/usr/local/bin/python2.7


import os

#Runs the Device Status Data
#os.system("spark-submit K-MeansMapCoord.deviceStatus.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/filteredStatus.csv 5 .1 GreateCircle @1.DeviceLocationDataClusters_GreateCircle")
#os.system("spark-submit K-MeansMapCoord.deviceStatus.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/filteredStatus.csv 5 .1 Euclidean @1.DeviceLocationDataClusters_Euclidian")


#Runs the All Data k = 2,3,4
#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 2 35 GreateCircle @1.GlobalClusters_GreateCircle_k2")
os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 3 .1 Euclidean @3.GlobalClusters_Euclidian_k3")
os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 2 .1 Euclidean @3.GlobalClusters_Euclidian_k2")

#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 3 35 Euclidean @1.GlobalClusters_Euclidian_k3")
#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 3 35 GreateCircle @1.GlobalClusters_GreateCircle_k3")

#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 4 .1 GreateCircle @1.GlobalClusters_GreateCircle_k4")

#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 5 .1 Euclidean @1.GlobalClusters_Euclidian_k6")
#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 5 .1 GreateCircle @1.GlobalClusters_GreateCircle_k6")

#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 6 .1 Euclidean @1.GlobalClusters_Euclidian_k6")
#os.system("spark-submit K-MeansMapCoord.DBpedia.py file:///home/training/K-MeansViaSpark/MileStone3/step3.Input/step3.filteredAll.csv 6 .1 GreateCircle @1.GlobalClusters_GreateCircle_k6")
