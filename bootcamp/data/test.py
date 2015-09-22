import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"
GENE_INFO = "gene_info.txt"
GO_INFO = "go_info.txt"
GO_MEMBERSHIP = "go_membership.txt"

def gene_to_go(gene):
	txt = open(GO_MEMBERSHIP)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	goids = []
	for i in range(0, numrows):
		if gene == datalist[i][0]:
			goids.append(datalist[i][1])
	
	return goids
	
	txt.close()
			
print gene_to_go("YAL001C")

