import csv
from collections import defaultdict
#with open('C:\Users\Gorgak\Downloads\CSV\test', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar="\"")
#    for row in spamreader:
#        print ', '.join(row)

dim1 = [1,2,3]
dim2 = [2,3,4]

dimsquared = []
dimsquared.append(dim1)
dimsquared.append(dim2)
print dimsquared[0][1]
'''
csv_path = __file__ + "\\..\\resource\\ShopifyWithVariants.csv"
image_path = __file__ + "\\..\\resource\\images\\"
handles = defaultdict(list)

print csv_path
with open(csv_path,'rb') as f:	
	rownum = 0
	reader = csv.reader(f)
	for row in reader:
#		if rownum == 1:
		if rownum >= 1:
			#print row[0]
			if row[0] not in handles:
				print "ADDING " + row[0] + " TO HANDLES"
				handles[row[0]] = [[]]
				for column in row:
					handles[row[0]][0].append(column)
				handles[row[0]].append(row)
#			if not row[1]
		rownum += 1
	for key in handles:
		print handles[key][0][3]
		break
'''