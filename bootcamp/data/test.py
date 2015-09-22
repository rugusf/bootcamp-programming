import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"

def gene_data(gene):
	txt = open(EXPERIMENT_FILE)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	for i in range(0, numrows):
		if gene == datalist[i][0]:
			datavals = datalist[i]
			return datavals[1:]
			
print gene_data("YAL001C")

