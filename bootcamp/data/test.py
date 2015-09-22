import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

GENE_INFO = "gene_info.txt"

def gene_name(gene):
	txt = open(GENE_INFO)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	genelist = []
	for row in range(1, numrows):
		pair = [datalist[row][0], datalist[row][1]]
		genelist.append(pair)
	
	for i in range(0, numrows - 1):
		if gene == genelist[i][0]:
			return genelist[i][1]
	
	txt.close()


print gene_name("YBR066C")
print "should be NRG2"
print gene_name("YCR093W")

