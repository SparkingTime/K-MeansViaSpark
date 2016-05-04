#MileStone 3



##Goals
  * [ ] Step1=>DeviceStatus
  * [x] Step2=>SampleGeo
  * [ ] Step3=>Real Data
  
##Scripts Lists

####[K-MeansMapCoord.py](./K-MeansMapCoord.py)
####[MapScatterVisulization.py](./MapScatterVisulization.py)
####[syntheticGeo.MapScatterVisulization](./syntheticGeo.MapScatterVisulization.py)
####[SampleGeoClustteringVisulizationK=4](https://plot.ly/445/%7Eseedbazzal/)

##Questions For TMR

----------

* Submission Procedure
   X 

* Geo-Median methods
  X

* 3D Visulization for extra credit?
  X

* *Sample the cluster because of the api limit*
Parse the 


* *Convergence Value* touse
X
* For the report. Is there anyway to analyize the quality of clustering except viewing it?
* Run-Time Analysis => (1) Clarifying (2) runing on different computers?
* 

The Run Time Analysis utilized the following command in order to determine the effects of different 

`spark-submit K-MeansMapCoord.py file:///home/training/K-MeansViaSpark/MileStone3/Input/step3.filteredAll.csv 4 25 GreateCircle`

| Program Run Stats        | Time Taken             | 
| ------------------------ |:----------------------:| 
| Single Core              | 9 min 40 secs          | 
| Dual Core                | 3 min 03 secs          | 
| Triple Core              | 3 min 02 secs          | 
| Quad Core                | 3 min 02 secs          |
| Penta Core               | 3 min 01 secs          |

*__Averaged over 5 Runs__
