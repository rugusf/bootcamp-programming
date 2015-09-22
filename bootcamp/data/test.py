import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"
GENE_INFO = "gene_info.txt"
GO_INFO = "go_info.txt"
GO_MEMBERSHIP = "go_membership.txt"

def go_aspect(aspect):
	txt = open(GO_INFO)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	gop = []
	gof = []
	goc = []
	for i in range(0, numrows):
		if datalist[i][2] == 'P':
			gop.append(datalist[i][0])
		elif datalist[i][2] == 'F':
			gof.append(datalist[i][0])
		elif datalist[i][2] == 'C':
			goc.append(datalist[i][0])
	
	if aspect == 'F':
		return gof
	elif aspect == 'P':
		return gop
	elif aspect == 'C':
		return goc
		
	txt.close()

print go_aspect('P')