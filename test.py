import csv
#with open('C:\Users\Gorgak\Downloads\CSV\test', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar="\"")
#    for row in spamreader:
#        print ', '.join(row)


file = open(__file__+"\\..\\resource\\keys.properties",'r')

print file.readline()
print file.readline()