### K-Means Clustering on large Geo data via Spark

---------

    @SeedofWind @Cogle @Mengnalin

####Introduction

######What is Clustering
Clustering is the task of grouping a set of objects in such a way that objects in the same cluster are more similar  to each other than to those in other clusters. 

While does not look like a complex problem to solve, it is often considered to be one of the most important unsupervised learning problem in machine larning. As as every other problem of this kind, it deals with finding a structure in a collection of unlabeled data. Following is an illustration of the process 

![alt text](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/images/clustering.gif "Clustering Illustration")

######Use cases of Clustering
Clustering algorithms can be applied in many fields, for instance:

* Marketing: finding groups of customers with similar behavior given a large database of customer data containing their properties and past buying records;
* Biology: classification of plants and animals given their features;
* Libraries: book ordering;
* Insurance: identifying groups of motor insurance policy holders with a high average claim cost; identifying frauds;
* City-planning: identifying groups of houses according to their house type, value and geographical location;
* Earthquake studies: clustering observed earthquake epicenters to identify dangerous zones;
* WWW: document classification; clustering weblog data to discover groups of similar access patterns.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="https://plot.ly/~rzbens/0.embed"></iframe>

================

####High-level Algorithm

As mentioned above, K-means clustering is quite intuitive and straightforward. Here we first introduce the high-level algorithm.


K-means in a "mapreduce" context is a little bit more invovled but goes as follows.

================

####Spark Implementation 

We choose Spark 

===============

####Results & Discussion

----

#####Step1-
----

#####Stpe2-
----

#####Step3-Runtime Analysis

----
####Conclusion
[RDD persistance with cache](http://http://spark.apache.org/docs/latest/programming-guide.html#rdd-persistence)


