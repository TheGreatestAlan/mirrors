import csv

csv_path = __file__ + "\\..\\resource\\ShopifyWithVariants.csv"
new_csv_path = __file__ + "\\..\\resource\\ShopifyWithVariantsImgAdjusted.csv"

r = csv.reader(open(csv_path))
lines = [l for l in r]
file_num = 1
for line in lines:
	if file_num > 14:
		file_num = 1
	line[42] = str(file_num) + ".jpg"
	file_num = file_num + 1
for line in lines:
	print line[42]

writer = csv.writer(open(new_csv_path,'w'))
writer.writerows(lines)