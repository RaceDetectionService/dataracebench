import json
import re
import sys


with open(sys.argv[1]) as test:
	data = test.read();
d = json.loads(data)
print(len(d))
#need a function to analysis the input
