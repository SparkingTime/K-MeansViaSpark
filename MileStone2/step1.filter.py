# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import argparse
from operator import add

from pyspark import SparkContext


def filtering(line):
    arr  = line.replace('|',',').split(',')

    if(len(arr)<14):
        return []
    if(arr[len(arr)-1]=="0" and arr[len(arr)-2]=="0"):
        return []
    else:
        return [arr[0]+","+arr[1]+","+arr[2]+","+arr[12]+","+arr[13]]
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: wordcount <file>"
        exit(-1)

    parser = argparse.ArgumentParser()
    sc = SparkContext(appName="PythonWordCount")
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
    filtered = lines.flatMap(filtering)
    print(filtered.count())
    output = filtered.collect()

    count = 0
    print("!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!")
    for i in output:
        count=count+1
        print(i)
        if(count==50):
            break

    if(location=="local"):
        location = location+"/home/training/Desktop/"

    filtered.saveAsTextFile("file:////home/training/Desktop/filtered_deviceStatus")
    sc.stop()
