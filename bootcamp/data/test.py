import os # a built-in module, for dealing with filenames
#from . import app # this is part of the website guts
import csv

EXPERIMENT_FILE = "experiment_data.txt"

dic = {}
def experiment():
    #experiments = []
    input_file = open (EXPERIMENT_FILE)
    #lines = exp_file.readlines()
    #for line in lines:
    data = csv.reader (input_file, delimiter='\t')
    #for column in data:
    #    for row in data:
    #        pair = [row[0], column[1]
    #for column in data:
    content = list(column)
    print content


experiment()
