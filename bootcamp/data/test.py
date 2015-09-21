import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"

def experiment():
	txt = open(EXPERIMENT_FILE)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	numcols = len(datalist[1])
	
	maplist = []
	for col in range(1, numcols):
		explist = []
		for row in range(1, numrows):
			pair = [datalist[row][0], datalist[row][col]]
			explist.append(pair)
		maplist.append(explist)
	
	print maplist
	print '-' * 100
	txt.close()


experiment()
