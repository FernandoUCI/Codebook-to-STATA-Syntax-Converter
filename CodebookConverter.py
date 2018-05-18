# Codebook Converter
# Please see README.md file prior to running
# Author: Fernando Rodriguez

# Lableing the variables # Lablei 
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