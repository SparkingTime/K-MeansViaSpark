##Output and Visulization Scripts

====

####Output folders

*  @1./@2./@3. describes which dataset the output corresponds to
  * @1.=>Device_Status
  * @2.=>Synthetic Location
  * @3.=>DBpedia

* k=n describes how many clusters we targeting for k-means

* GreatCircle/Euclidean stands for what distance measuremnt used

* For Instance
  [@3.GlobalClusters_GreateCIrcle_k6](https://github.com/SparkingTime/K-MeansViaSpark/tree/master/MileStone3/step3.Output/%403.GlobalClusters_GreateCircle_k6)stands for **output for DBpedia data, with 6 clusters using greateCircle measurement**

----

####Visulization Scripts

* Anything start with @1/@2/@3 and ends with .py is a Visulization python script for corresponding data
* Pass in an argument describe which distance measurment used

====

* For instance
  [@2.synthetic.py](https://github.com/SparkingTime/K-MeansViaSpark/blob/master/MileStone3/step3.Output/%402.synthetic.py)is the visulization script for Synthetic Location data output
  
  To run it do 

  ```
  python @2.synthetic.py GreateCircle/Euclidean
  ```
