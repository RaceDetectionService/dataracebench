import json
import re
import sys

file = open(sys.argv[1],"r")
Lines = file.readlines()
jsAry = []
content = [line.strip() for line in Lines]
for i in range(0,len(content)):
	x = re.search("^Write",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		js = {}
		js["Memory Address"] = y[index+1]
		index1 = y.index('by')
		Thread = re.split(":",y[index1+2])
		js["Write_thread"] = y[index1+1] + ' ' + Thread[0]
		y1 = content[i+1].split()
		for item in y1:
			if(re.search("^/",item)):
				file = item.rsplit("/",1)
				js["file loaction"] = file[0]
				location = file[1].split(":")
				js["write file name"] = location[0]
				js["write line #"] = location[1]
				if len(location) >= 3:
					js["write column #"] = location[2]
				else:
					js["write column #"] = -1
		jsAry.append(js)
	x = re.search("^Previous read",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		for item in jsAry:
			if (item["Memory Address"] == y[index+1]):
				index1 = y.index('by')
				Thread = re.split(":",y[index1+2])
				item["Read_thread"] = y[index1+1] + ' ' + Thread[0]
				y1 = content[i+1].split()
				for item1 in y1:
					if(re.search("^/",item1)):
						file = item1.rsplit("/",1)
						location = file[1].split(":")
						item["read file name"] = location[0]
						item["read line #"] = location[1]
						if len(location) >= 3:
							js["Read column #"] = location[2]
						else:
							js["Read column #"] = -1
						item["tool"] = "Archer"
		
	x = re.search("^Read",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		js = {}
		js["Memory Address"] = y[index+1]
		index1 = y.index('by')
		Thread = re.split(":",y[index1+2])
		js["Write_thread"] = y[index1+1] + ' ' + Thread[0]
		y1 = content[i+1].split()
		for item in y1:
			if(re.search("^/",item)):
				file = item.rsplit("/",1)
				js["file loaction"] = file[0]
				location = file[1].split(":")
				js["Read file name"] = location[0]
				js["Read line #"] = location[1]
				if len(location) >= 3:
					js["Read column #"] = location[2]
				else:
					js["Read column #"] = -1
		jsAry.append(js)
	x = re.search("^Previous write",content[i])
	if (x):
		y = content[i].split()
		index = y.index('at')
		for item in jsAry:
			if item["Write_thread"] is not None:
				if (item["Memory Address"] == y[index+1]):
					index1 = y.index('by')
					Thread = re.split(":",y[index1+2])
					item["Write_thread1"] = y[index1+1] + ' ' + Thread[0]
					y1 = content[i+1].split()
					for item1 in y1:
						if(re.search("^/",item1)):
							file = item1.rsplit("/",1)
							location = file[1].split(":")
							item["write file name1"] = location[0]
							item["write line #1"] = location[1]
							if len(location) >= 3:
								js["write column #1"] = location[2]
							else:
								js["write column #1"] = -1
							item["tool"] = "Archer"
			elif (item["Memory Address"] == y[index+1]):
				index1 = y.index('by')
				Thread = re.split(":",y[index1+2])
				item["Write_thread"] = y[index1+1] + ' ' + Thread[0]
				y1 = content[i+1].split()
				for item1 in y1:
					if(re.search("^/",item1)):
						file = item1.rsplit("/",1)
						location = file[1].split(":")
						item["write file name"] = location[0]
						item["write line #"] = location[1]
						if len(location) >= 3:
							js["write column #"] = location[2]
						else:
							js["write column #"] = -1
						item["tool"] = "Archer"


js = {}
for i in range(len(jsAry)):
	js[i] = jsAry[i]

r = json.dumps(js)
print(r)
