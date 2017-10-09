import sys, re
import math

def CheckTop5(ED, TopFive):
	check  = 1
	TopFive.append(ED)
	TopFive.sort()
	TopFive.pop(0)
# argv[1] is the input file, argv[2] is the output file which added mpg information
fin = open(sys.argv[1],'r')
#fin = open('SFOData.tsv','r')
fout = open(sys.argv[2],'w')
store = []
for line in fin:
	line = line.rstrip()
	store.append(line)


for car in store:
	print "car being Compared: " + car
	carFields = re.split("\t", car)
	TopFive = []
	for i in xrange(0,len(store)):
		fields = re.split("\t", store[i])
		if fields[0] != carFields[0]:
			euclideanDistance  = 0
			for j in range(3,6):
				diff = int(carFields[j]) - int(fields[j])
				euclideanDistance = euclideanDistance + diff*diff
			euclideanDistance = math.sqrt(euclideanDistance)
			car = fields[1] + "-" + fields[2] + "-" + fields[3]
			print car  + "\t" + str(euclideanDistance)
			tup = (euclideanDistance, car)
			TopFive.append(tup)
			TopFive.sort()
			if len(TopFive) > 5:
				TopFive.pop()
	string = "\t".join(carFields)
	string2 = ""
	for tup in TopFive:
		string2 =  string2 + "\t" + tup[1]
	fout.write("\t".join([string,string2]))
	fout.write("\n")