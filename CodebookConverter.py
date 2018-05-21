# Codebook Converter
# Please see README.md file prior to running
# Author: Fernando Rodriguez


# list files in a directory using :os.path.join
import os

# import csv files
import csv


# file directory
data_dir = "/Users/fernanr1/Google Drive/Python Workspace/Codebook Converter - 11-15-17/"


# file name
csv_file = os.path.join(data_dir, "codebook_file.csv")
type(csv_file)


# Checking that we are able to successfully read the first colum of our CSV file
with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter = ',') # saving contents to variable 'reader'
    for line in reader:
        print line[0] # reading the first column



# Getting a list of all of the response options
with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    header = reader.next()
    for line in reader:
        responseopt = line[2]
        print responseopt

# Getting a list of unique response options
# These will be the values for the key:value pairs
responses = []

with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    header = reader.next()
    for line in reader:
        if line[2] not in responses:
            responses.append(line[2])

print responses


# Generating 100 labelids which will serve as the keys for the key:value pair# Genera
labelid = []
labelnum = 1
for x in range(1, 101):
    res = ("labelname" + `labelnum`)
    labelnum += 1
    labelid.append(res)
print(labelid[:10])


# Creating label dictionary by combining the label id (key) and responses (values)
labeldict = dict(zip(labelid, responses))
print labeldict



# 1) Defining the response options
print "*** DEFINING LABELS FOR EACH UNIQUE RESPONSE OPTIONS ***"
print ""
for x in labeldict:
    print "label define", x, str(labeldict[x])
    print ""
print ""
print ""


# 2) Lableing the variables
print "*** DATA LABELING ***"
print ""
with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    header = reader.next()
    for line in reader:
        labels = str(line[0])+"label" # making a label name for STATA
        print "*", line[0], "data label"
        print "label variable", line[0], '"%s"' % line[1]
        for keylist, valuelist in labeldict.items():
            if valuelist == str(line[2]):
                print "label values", keylist
        print""
