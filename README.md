
## K-Means Clustering on large Geo data via Spark

--------- 

    @SeedofWind @Cogle @Mengnalin

#### Introduction

##### What is Clustering
-----
Clustering is the task of grouping a set of objects in such a way that objects in the same cluster are more similar  to each other than to those in other clusters. 

While does not look like a complex problem to solve, it is often considered to be one of the most important unsupervised learning problem in machine larning. As as every other problem of this kind, it deals with finding a structure in a collection of unlabeled data. Following is an illustration of the process 

![alt text](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/images/clustering.gif "Clustering Illustration")

##### Goals of Clustering
----
So, the goal of clustering is to determine the intrinsic grouping in a set of unlabeled data. But how to decide what constitutes a good clustering? It can be shown that there is no absolute “best” criterion which would be independent of the final aim of the clustering. Consequently, it is the user which must supply this criterion, in such a way that the result of the clustering will suit their needs.
For instance, we could be interested in finding representatives for homogeneous groups (data reduction), in finding “natural clusters” and describe their unknown properties (“natural” data types), in finding useful and suitable groupings (“useful” data classes) or in finding unusual data objects (outlier detection).


##### Use cases of Clustering
----
Clustering algorithms can be applied in many fields, for instance:

* Marketing: finding groups of customers with similar behavior given a large database of customer data containing their properties and past buying records;
* Biology: classification of plants and animals given their features;
* Libraries: book ordering;
* Insurance: identifying groups of motor insurance policy holders with a high average claim cost; identifying frauds;
* City-planning: identifying groups of houses according to their house type, value and geographical location;
* Earthquake studies: clustering observed earthquake epicenters to identify dangerous zones;
* WWW: document classification; clustering weblog data to discover groups of similar access patterns.

##### Purpose of this project
------
In this project, we implement an iterative algorithm (simple K-means) via **Spark** that solves the clustering problem in a parallel fashion. Details about K-means algorithm and the reason why we chose Spark will be discussed later.

================

#### High-level k-Means Algorithm
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

##### Mapper Phase
* Read the cluster centers into memory from a sequencefile
* Iterate over each cluster center for each input key/value pair. 
* Measure the distances and save the nearest center which has the lowest distance to the vector
* Write the clustercenter with its vector to the filesystem.

##### Reduce Phase
* Iterate over each value vector and calculate the average vector. (Sum each vector and devide each part by the number of vectors we received).
* This is the new center, save it into a SequenceFile.
* Check the convergence between the clustercenter that is stored in the key object and the new center.
    * If it they are not equal, increment an update counter
* Run this whole thing until nothing was updated anymore.


================

#### Spark Implementation (Python Wrapper)

We choose Spark because compared to tool like hadoop, it is much better platform to do machine learning. We can easily reuse the data from one job by reading it directly from the cache. How Spark achived this **will be discussed in detail** in later section.
Moreover, Spark is a important tool to learn, since essentially, it is more general, more flexible and no offense, better than hadoop mapreduce in almost every measure except legacy reaons.

Specifically, we use the python wrapper to interact with spark. THis is because we are more famialiar with python compared to scala. While funcional language is something on my list to learn. For now, i ma gonna stay in my comfort zone.

===============

#### Results & Discussion

----

##### Step1- Understanding Parallel Data Processing and Persisting RDDs

Spark is fast. At the core of Spark's speed lies the RDD. In this section we will exam the resilient distributed dataset(RDD), and 
look at how this abstraction is responsible for the large performance differences that exist between Spark and Hadoop.  

Our first step is to understand what an RDD is. At a high level an RDD is an **immutable** distributed collection of objects. Spark, like Hadoop MapReduce, is a way of computing data on a distributed computing system. When an RDD is created in Spark it is created such that it is **partionable**; this means that when running a task Spark can split up an RDD and distributed it across various compute nodes within the cluster. For those that are familiar with Hadoop this may not seem like a revolutionary idea, MapReduce based off a similar idea. The difference between the two lies in how the data is stored. 

In Spark the RDD allows the the program to **cache** a particular partion on a node. This __peristance__ of data allows us to reuse data over and over in our operations. This persistance of data allows us to implement iterative algorithms with ease. Instead of being bottlenecked by I/O operations and the associated network throughput to transfer large quanities of data it can all be stored on a node and reused. This is a key difference from the Hadoop MapReduce ideology. In MapReduce everything must be written out to a file.; this involves large amounts of network traffic as data must be transported across the network. In addition I/O operation are notoriously slow so elminating these operations speeds up our time tremendously. 



##### Step2- Understanding and Implementing k-means

K-means is one of the best known family of clustering algorithms. The heart of the algorithm is the for-loop, in which we consider each point other than the k selected points and assign it to the closest cluster, where closest here closest to the centroid of the cluster. The centroid of the cluster can migrate as points are assigned to it. However, the centroid tends not to move too much because points near the cluster are likely to be assigned. 
Here we implement a function to retrieve latitude and longitude of every record in the target data. Then we choose k initial cluster centers at random by build-in function takeSample. We create mapper output (key is index of point and value is (index of closest center, 1, point in list format)) by choosing corresponding cluster center that is closest to the point. Reducer output is created by reduceByKey function. Then new cluster center is calculated by average all data in one cluster. Temporary distance is calculated by adding all distances between data and the corresponding cluster centers. If the distance is smaller than the previous one then we just update it. We iterate through while loop until difference between previous distance and current one meet certain condition. We use two methods to calculate distance between two data points( Euclidean Distance and Great Circle Distance) depending on the input. Details can be found [here]:()


##### step3- Compute and Visulize 


* Here, we present our clustering and visulization results for **Sample Geo, Device LOcation, and DBpedia data**. For each    data, we cluster it by GreatCircle Distance and Euclidean distance to understand which generates a better clustering (in    theory, GreatCircle Distance is a more accurate measurement). 

* **Three IMPORTANT NOTES**
 * Since the datas for Device Location and DBpedia is very large, during the visulization of each cluster, we randomly        sample 0.1 of the points in the cluster
 * For centers_comparison plot, trace0 is centers computed from Euclidean method while trace1 is from Greatcircle(Diamond     Shape)
 * All converge Distance is set to be 0.1km
 
* For each k value, we will present visulization via both distance Methods, namely GreatCircle and Euclidean, and also a      plot comparing the final centers derived from two methods

* For each part, a brief summary about the observation will be given in the end
* For DBpedia Data, since we are trying to understand what k gives out better clustering k = 2,3,4,5,6 will be presented and   a discussion about which, from our perspective yields a better clustering will be prestned in the end of the part

###### part@1-Device Data
 
 **Cluster and Visualize the [Device Status data](./step3.Input/filteredStatus.csv)**

====

1.  k = 5 DistanceMethod = GreatCircle

    The output (divided to 5 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output)
    
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/463/devicestatus-k-5-clustering-via-greatecircle/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%401.DeviceStatus_k%3D5_GreateCircle.png "Device Status clustering GreateCircle")

2.  k = 5 DistanceMethod = Euclidean

    The output (divided to 5 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output)
    
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/461/devicestatus-k-5-clustering-via-euclidian/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%401.DeviceStatus_k%3D5_Euclidian.png "Device Status clustering Euclidean")

3. Two-methods Centers Comparision
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/459/devicestatus-k-5-clustering-centers-comparision-euclidean-vs-great-circle/)   
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%401.DeviceStatus_k%3D5_centers.png "Device Status clustering")

* Summary
  In the visulization of the clustering via two methods, we can find data points are clustered differently via two distance measure. However, both returns logical clustering. One might argue that GreatCircle, in this particular case did a better job in the sense that the yellow cluster is more centered. However,it is not consistant that GreatCircle always yields better clustering (can be seen in the later sections)

---

###### part@2-Synthetic Data

*Cluster and Visualize the [Syntheic Geo data](./step3.input/step2.sample_geo.csv)*

====

K-means clustering on this data converges nicely with a converge distance 0.1 (unlike the global data that contain points seperates further apart). We clustered it into 4 clusters (k=4) via both Euclidean Distance and Greate Circle Distance .

1.  k = 4 DistanceMethod = GreatCircle

    The output (divided to 4 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output)
    
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/465/syntheticlocation-clustering-via-greatecircle/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%402.SampleGeoClusteringEuclidian.png "Syntheic Geo clustering GreateCircle")

2.  k = 4 DistanceMethod = Euclidean

    The output (divided to 4 files and 1 center file) can be seen [here](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output)
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/449/syntheticlocation-clustering-via-euclidean/)
    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%402.SampleGeoClusteringEuclidian.png "Syntheic Geo clustering Euclidean")

3. Two-methods Centers Comparision
    Following is the visulization. A more detailed plot(full-featured interactive explore) can be found [here](https://plot.ly/~seedbazzal/459/devicestatus-k-5-clustering-centers-comparision-euclidean-vs-great-circle/)   
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%401.DeviceStatus_k%3D5_centers.png "Device Status clustering")

* Summary
  K-means clustering on this data converges nicely with a converge distance 0.1 in only 5 iterations (unlike the global data that contain points seperates further apart). We clustered it into 4 clusters (k=4) via both Euclidean Distance and Greate Circle Distance. It is clear that in this case, both methods yields very similar result and both did a great job in terms of clustering.
  
  

---

###### part@3-DBpedia Data

*Cluster and Visualize the [DBpedia data](./step3.filteredAll.csv)*

====



1.  k = 2 DistanceMethod = GreatCircle


    
    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D2Euclidian.png "All data k =2 GreateCirlce")

2.  k = 2 DistanceMethod = Euclidean

   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D2Euclidian.png "All data k =2 GreateCirlce")
   
*  Two-methods Centers Comparision
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D2_Cluster_Centers.png "All data k =2 center comparision")    

   
    
3.  k = 3 DistanceMethod = GreatCircle


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D3_GreateCircle.png "All data k =3 GreateCirlce")
    

4.  k = 3 DistanceMethod = Euclidean


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D3_Euclidean.png "All data k =3 Euclidean")

*  Two-methods Centers Comparision
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D3_Centers.png "All data k =3 center comparision")    
    
5.  k = 4 DistanceMethod = GreatCircle


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D4_GreateCircle.png "All data k =4 GreateCirlce")
    

6.  k = 4 DistanceMethod = Euclidean


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D4_Euclidean.png "All data k =4 GreateCirlce")
    
*  Two-methods Centers Comparision
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D4_Centers.png "All data k =4 center comparision")    

7.  k = 5 DistanceMethod = GreatCircle


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D5_GreatCircle.png "All data k =5 GreateCirlce")
   
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D5_GreatCircleFlat.png "All data k =5 GreateCirlce")
    
8.  k = 5 DistanceMethod = Euclidean


   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D5_Euclidean.png "All data k =5 Euclidiean")
    
*  Two-methods Centers Comparision
   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D5_Centers.png "All data k =5 center comparision")

9.  k = 6 DistanceMethod = GreatCircle

    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D6GreatCircle.png "All data k =6 GreatCircle")

10.  k = 6 DistanceMethod = Euclidean

    ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D6Euclidian.png "All data k =6 Euclidean")

* Two-methods Centers Comparision

   ![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%403.All_k%3D6_Cluster_Centers.png "All data k =6 Centers")

============

**Summary**
Several interesting findings from this large data set. 
* k = 2 to 4 takes longer iterations (40-70) to conerge since points tend to more farther apart
* k = 6 is arguebaly the best clusters value (while 5 is also pretty good)
* We can see that GreatCircle measurment is not giving us a better result compared to simple Euclidean calculation
* **IN GENERAL**, Euclidean measurement concerges quicker

---

###### Step4- Runtime Analysis

The Run Time Analysis utilized the following command in order to determine the effects of different 
    
`time spark-submit K-MeansMapCoord.py file:///home/training/K-MeansViaSpark/MileStone3/Input/step3.filteredAll.csv 4 25 GreateCircle`

| Program Run Stats        | Time Taken             | 
| ------------------------ |:----------------------:| 
| Single Core              | 9 min 40 secs          | 
| Dual Core                | 3 min 03 secs          | 
| Triple Core              | 3 min 02 secs          | 
| Quad Core                | 3 min 02 secs          |
| Penta Core               | 3 min 01 secs          |
| Not Caching              | Not progressing after waiting for 15 min|
*__Averaged over 5 Runs__


----


#### Extra Analysis

===

###### Different Initialization centers analysis
We try to understand whether different initialization will yields different clustering results both in terms of outcome and performance

* trace 0 -- initial 4 points are as farther apart as possible via a greedy algorithm
* trace 1 -- initial 4 points are as farther apart as possible handpicked
* trace 2 -- random trace
* trace 3 -- random trace
* trace 4 -- random trace

![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/InitialTests.png "Synthetic Location")

**Observations**

* In terms of *Performance*, no significant difference is observed
* In terms of *outcome*, they are pretty similar

###### 3D visulization

Here, we use 3D projection to Visualize our data

![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/extra_3d1.png "All data k =6 Centers")

====

![alt text](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/extra3d.png "All data k =6 Centers")


--------
======

#### Conclusion

* In this project we have successfully use Spark to implement K-means Clustering on all three data sets
* Detailed findings and observations can be found in corresponding sections
* in conclusion, Spark is a nice tool for doing machine learning!
