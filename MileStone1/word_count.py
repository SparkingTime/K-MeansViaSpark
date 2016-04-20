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
    counts = lines.flatMap(lambda x: x.split(' ')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print "%s: %i" % (word, count)

    sc.stop()