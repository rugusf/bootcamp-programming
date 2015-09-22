import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"
GENE_INFO = "gene_info.txt"
GO_INFO = "go_info.txt"
GO_MEMBERSHIP = "go_membership.txt"

def go_info(goid):
	txt = open(GO_INFO)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)

	for i in range(0, numrows):
		if goid == datalist[i][0]:
			goidinfo = datalist[i]
			return goidinfo[1:]
			
	txt.close()
	
	
print go_info("GO:0000015")