##To do
*  Visulization of geo (euclidean)
*  VIsulization of deviceStatus
*  All data?
*  Run time analysis no cache

## K-Means Clustering on large Geo data via Spark

--------- 

    @SeedofWind @Cogle @Mengnalin

####Introduction

#####What is Clustering
-----
Clustering is the task of grouping a set of objects in such a way that objects in the same cluster are more similar  to each other than to those in other clusters. 

While does not look like a complex problem to solve, it is often considered to be one of the most important unsupervised learning problem in machine larning. As as every other problem of this kind, it deals with finding a structure in a collection of unlabeled data. Following is an illustration of the process 

![alt text](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/images/clustering.gif "Clustering Illustration")

#####Goals of Clustering
----
So, the goal of clustering is to determine the intrinsic grouping in a set of unlabeled data. But how to decide what constitutes a good clustering? It can be shown that there is no absolute “best” criterion which would be independent of the final aim of the clustering. Consequently, it is the user which must supply this criterion, in such a way that the result of the clustering will suit their needs.
For instance, we could be interested in finding representatives for homogeneous groups (data reduction), in finding “natural clusters” and describe their unknown properties (“natural” data types), in finding useful and suitable groupings (“useful” data classes) or in finding unusual data objects (outlier detection).


#####Use cases of Clustering
----
Clustering algorithms can be applied in many fields, for instance:

* Marketing: finding groups of customers with similar behavior given a large database of customer data containing their properties and past buying records;
* Biology: classification of plants and animals given their features;
* Libraries: book ordering;
* Insurance: identifying groups of motor insurance policy holders with a high average claim cost; identifying frauds;
* City-planning: identifying groups of houses according to their house type, value and geographical location;
* Earthquake studies: clustering observed earthquake epicenters to identify dangerous zones;
* WWW: document classification; clustering weblog data to discover groups of similar access patterns.

#####Purpose of this project
------
In this project, we implement an iterative algorithm (simple K-means) via **Spark** that solves the clustering problem in a parallel fashion. Details about K-means algorithm and the reason why we chose Spark will be discussed later.

================

####High-level k-Means Algorithm
-----
As mentioned above, K-means clustering is quite intuitive and straightforward. Here we first introduce the high-level algorithm.

1. Randomly select ‘c’ cluster centers.
2. Calculate the distance between each data point and cluster centers.
3. Assign the data point to the cluster center whose distance from the cluster center is minimum of all the cluster centers.
4. Recalculate the new cluster centers using 

        V_i = Sum(x_i)/count(i)

5. Recalculate the distance between each data point and new obtained cluster centers.
6. If no data point was reassigned then stop, otherwise repeat from step (3).

K-means in a "mapreduce" context is a little bit more invovled but goes as follows.

#####Mapper Phase
* Read the cluster centers into memory from a sequencefile
* Iterate over each cluster center for each input key/value pair. 
* Measure the distances and save the nearest center which has the lowest distance to the vector
* Write the clustercenter with its vector to the filesystem.

#####Reduce Phase
* Iterate over each value vector and calculate the average vector. (Sum each vector and devide each part by the number of vectors we received).
* This is the new center, save it into a SequenceFile.
* Check the convergence between the clustercenter that is stored in the key object and the new center.
    * If it they are not equal, increment an update counter
* Run this whole thing until nothing was updated anymore.


================

####Spark Implementation (Python Wrapper)

We choose Spark 

===============

####Results & Discussion

----

#####Step1- Understanding Parallel Data Processing and Persisting RDDs

Spark is fast. At the core of Spark's speed lies the RDD. In this section we will exam the resilient distributed dataset(RDD), and 
look at how this abstraction is responsible for the large performance differences that exist between Spark and Hadoop.  

Our first step is to understand what an RDD is. At a high level an RDD is an **immutable** distributed collection of objects. Spark, like Hadoop MapReduce, is a way of computing data on a distributed computing system. When an RDD is created in Spark it is created such that it is **partionable**; this means that when running a task Spark can split up an RDD and distributed it across various compute nodes within the cluster. For those that are familiar with Hadoop this may not seem like a revolutionary idea, MapReduce based off a similar idea. The difference between the two lies in how the data is stored. 

In Spark the RDD allows the the program to **cache** a particular partion on a node. This __peristance__ of data allows us to reuse data over and over in our operations. This persistance of data allows us to implement iterative algorithms with ease. Instead of being bottlenecked by I/O operations and the associated network throughput to transfer large quanities of data it can all be stored on a node and reused. This is a key difference from the Hadoop MapReduce ideology. In MapReduce everything must be written out to a file.; this involves large amounts of network traffic as data must be transported across the network. In addition I/O operation are notoriously slow so elminating these operations speeds up our time tremendously. 

----

#####Step2- Understanding and Implementing k-means


#####step3- Compute and Visulize 


* Here, we present our clustering and visulization results for **Sample Geo, Device LOcation, and DBpedia data**. For each    data, we cluster it by GreatCircle Distance and Euclidean distance to understand which generates a better clustering (in    theory, GreatCircle Distance is a more accurate measurement). 

* For K-means on DBPedia Data, we run throuhg k=2, k=3, k=4, k=5 , k=6 to understand which cluster number clustering the data better. Also for each k, we run K-means using GreateCircle and Euclidean distance measure
* In each part, we will first present our data and visulization for each k and each distance measure then conclude with a breif summary


######part@2-Synthetic Data

*Cluster and Visualize the [Syntheic Geo data](./step3.input/step2.sample_geo.csv)*

K-means clustering on this data converges nicely with a converge distance 0.1 (unlike the global data that contain points seperates further apart). We clustered it into 4 clusters (k=4) via both Euclidean Distance and Greate Circle Distance .

1.  k = 4 DistanceMethod = GreateCircle

    The output (divided to 4 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output/%401.DeviceLocationDataClusters_GreateCircle)
    
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/445/%7Eseedbazzal/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%402.SyntheticLocationVisulization.png "Syntheic Geo clustering")

2.  k = 4 DistanceMethod = Euclidean
    The output (divided to 4 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output/%401.DeviceLocationDataClusters_GreateCircle)
    
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/445/%7Eseedbazzal/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%402.SyntheticLocationVisulization.png "Syntheic Geo clustering")

---

######Step4- Runtime Analysis

The Run Time Analysis utilized the following command in order to determine the effects of different 
    
`time spark-submit K-MeansMapCoord.py file:///home/training/K-MeansViaSpark/MileStone3/Input/step3.filteredAll.csv 4 25 GreateCircle`

| Program Run Stats        | Time Taken             | 
| ------------------------ |:----------------------:| 
| Single Core              | 9 min 40 secs          | 
| Dual Core                | 3 min 03 secs          | 
| Triple Core              | 3 min 02 secs          | 
| Quad Core                | 3 min 02 secs          |
| Penta Core               | 3 min 01 secs          |

*__Averaged over 5 Runs__


----
####Conclusion



