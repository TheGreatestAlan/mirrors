import shopify
import csv
from collections import defaultdict

#loading key file in the resource directory.
#remember to keep the resource directory in your .gitignore file
file = open(__file__+"\\..\\resource\\keys.properties",'r')
code1 = file.readline()
code2 = file.readline()

#connecting to shopfiy
shop_url = "https://%s:%s@wall-mirror-store.myshopify.com/admin" % (code1,code2)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()

csv_path = __file__ + "\\..\\resource\\ShopifyWithVariants.csv"
image_path = __file__ + "\\..\\resource\\images\\"

handles = defaultdict(list)
#looping through csv
with open(csv_path,'rb') as f:	
	rownum = 0
	reader = csv.reader(f)
	for row in reader:
#		if rownum == 1:
		if rownum >= 1:
			if row[0] not in handles:
				handles[row[0]] = [[]]
				for column in row:
					handles[row[0]][0].append(column)
				handles[row[0]].append(row)
			else:
				#Fuck, figure this out later, it's 4dub
				for column in row:
					handles[row[0]][]
		rownum += 1

for product in handles:
	#if the title is not null or empty (i.e. I'm taking this to be the base product)
	print handles[product][0][8]
	if not handles[product][0][1]:
		print handles[product][0][8]

'''
	new_product = shopify.Product()
	#add title, etc.
	new_product.handle = row[0]
	new_product.title = row[1]
	new_product.save()
	print(new_product.id)
	new_product.body_html = row[2]
	new_product.vendor = row[3]
	new_product.type = row[4]
	new_product.tags = row[5]
#			new_product.description = row[28]
	v = shopify.Variant(dict(price=row[19], option1="First", product_id=new_product.id))
	new_product.variants = [v]
	filename = image_path + row[24]
	print filename
#			    filename = path.split("\\")[-1:][0]
	image = shopify.Image()
	with open(filename, "rb") as f:
	    image.attach_image(f.read(), filename=filename)
	new_product.images = [image]
	success = new_product.save()
	print success

'''