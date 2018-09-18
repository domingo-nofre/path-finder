import sys
import re
from helpers import *


def process_line(line):
    m = re.match('[A-H]+[1-8]+ +[A-H]+[1-8]', line)
    if m:
        origin = line[0:2]
        destination = line[3:5]
        print(calculate_path(origin, destination))
        return 0
    else:
        print("Error format, please insert to chess positions "
              "separated by whitespace. F.e.: F3 D5")
    return


for line in sys.stdin:
    process_line(line)
