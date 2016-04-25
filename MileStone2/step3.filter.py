import sys
import argparse
#import googlemaps

from pyspark import SparkContext

def regularFilter(array):
	if len(array) == 3:
            return True
	return False


def inUnitedStates(array):
    if len(array) != 3:
        return False
    lat = float(array[0])
    lng = float(array[1])
    if lat < 49.0 and lat > 18.0 and lng > -124.7 and lng < -62.2:
        return True
    return False

def getInfoWanted(array):

    id = (array[-1]).encode('utf-8').split('/')

    info = id[-1]
    info = info.replace(',','')
    info = info.replace('>','')
    return  str(array[0])+ "," +str(array[1]) +"," + info


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: DBperdiaParse <file>"
        exit(-1)

    parser = argparse.ArgumentParser()
    sc = SparkContext(appName="PythonDBpediaParse")
    parser.add_argument("location" , help = " hdfs?local", type = str )
    parser.add_argument("path" , help = " hdfs?local", type = str )
    args = parser.parse_args()
    location = args.location;
    if(location == "local"):
        location = "file:///"
    else:
        location = ""

    filepath = args.path

    lines = sc.textFile(location+filepath)
    all_data = lines.map(lambda line: line.split(" ")).filter(regularFilter).map(getInfoWanted)
    usa_data = lines.map(lambda line: line.split(" ")).filter(inUnitedStates).map(getInfoWanted)


    if(location=="local"):
        location = location+"/home/training/Desktop/"

    all_data.saveAsTextFile("file:////home/training/Desktop/filtered_all")
    usa_data.saveAsTextFile("file:////home/training/Desktop/filtered_usa")
    sc.stop()
