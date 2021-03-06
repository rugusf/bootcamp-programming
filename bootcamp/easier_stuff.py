# coding: utf-8

# This file is for those of you who learned Python over the summer (you did that, right?).
# In this file, I've put all of the nitty-gritty details of what makes this website work.

# Except it doesn't work, because you need to write all the functions!

# Some of these functions will just make the website easier to use. Some of them are
# important for the enrichment and clustering tasks that your teammates are working on.

# If you need any help, ask your team or a TA.


# (don't delete this but don't worry about it either)
import os # a built-in module, for dealing with filenames
from . import app # this is part of the website guts

import csv




# These are all the files you have to work with. Go open them in a text editor so you can
# get a feel for what they look like, because you need to parse each one to turn on a
# piece of the website.

# A list of yeast genes, with standard names and short descriptions.
GENE_INFO = os.path.join(app.root_path, 'data', 'gene_info.txt')

# A file that maps from GOID to name, aspect (process/function/component), etc
GO_INFO = os.path.join(app.root_path, 'data', 'go_info.txt')

# A two-column file that maps GOID to yeast genes
GO_MEMBERSHIP = os.path.join(app.root_path, 'data', 'go_membership.txt')

# A many-columned file that contains experimental data (yeast microarrays). Each column
# (after the first) is a different experiment, and each row is a gene. The values are log2
# ratios versus untreated control.
EXPERIMENT_FILE = os.path.join(app.root_path, 'data', 'experiment_data.txt')


# return a list or dictionary that maps from the id of an experiment (an int: 0, 1, ..)
# to a list of (systematic name, fold-change value) tuples
# e.g. [[('YAL001C', -0.06), ('YAL002W', -0.3), ('YAL003W', -0.07), ... ],
#       [('YAL001C', -0.58), ('YAL002W', 0.23), ('YAL003W', -0.25), ... ],
#        ... ]
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
	
	txt.close()


# map from a gene's systematic name to its standard name
# e.g. gene_name('YGR188C') returns 'BUB1'
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


# map from a gene's systematic name to a list of the values for that gene,
# across all of the experiments.
# e.g. gene_data('YGR188C') returns [-0.09, 0.2, -0.07, ... ]
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
			
	txt.close()


# map from a systematic name to some info about the gene (whatever you want),
# e.g  'YGR188C' -> 'Protein kinase involved in the cell cycle checkpoint into anaphase'
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


# map from a systematic name to a list of GOIDs that the gene is associated with
# e.g. 'YGR188C' -> ['GO:0005694', 'GO:0000775', 'GO:0000778', ... ]
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


# map from one of the GO aspects (P, F, and C, for Process, Function, Component),
# to a list of all the GOIDs in that aspect
# e.g. 'C' -> ['GO:0005737', 'GO:0005761', 'GO:0005763', ... ]
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



# map from a GOID (e.g. GO:0005737) to a *tuple* of the term, aspect, and term definition
# e.g. 'GO:0005737' -> ('cytoplasm', 'C', 'All of the contents of a cell... (etc)'
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

# the reverse of the gene_to_go function: map from a GOID
# to a list of genes (systematic names)
# e.g. 'GO:0005737' -> ['YAL001C', 'YAL002W', 'YAL003W', ... ]
def go_to_gene(goid):
    txt = open(GO_MEMBERSHIP)
	data = csv.reader(txt, delimiter = '\t')
	
	datalist = []
	for row in data:
		datalist.append(row)
	numrows = len(datalist)
	
	gene_name = []
	for i in range(0, numrows):
		if goid == datalist[i][1]:
			gene_name.append(datalist[i][0])
	
	return gene_name
	
	txt.close()
