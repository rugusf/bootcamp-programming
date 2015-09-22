import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"
GENE_INFO = "gene_info.txt"

def gene_info(gene):
	txt = open(GENE_INFO)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	for i in range(0, numrows):
		if gene == datalist[i][0]:
			geneinfo = datalist[i]
			return geneinfo[2:]
			
	txt.close()
			
print gene_info("YAL001C")

