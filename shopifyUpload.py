import shopify
import csv
#with open('C:\Users\Gorgak\Downloads\CSV\test', 'rb') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',', quotechar="\"")
#    for row in spamreader:
#        print ', '.join(row)

file = open(__file__+"\\..\\resource\\keys.properties",'r')
code1 = file.readline()
code2 = file.readline()
shop_url = "https://%s:%s@wall-mirror-store.myshopify.com/admin" % (code1,code2)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()

csv_path = __file__ + "\\..\\resource\\Shopify Test Products Backup 7-5-15.csv"
image_path = __file__ + "\\..\\resource\\images\\"

print csv_path
with open(csv_path,'rb') as f:	
	rownum = 0
	reader = csv.reader(f)
	for row in reader:
#		if rownum == 1:
		if rownum >= 1:
			print row[19]
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
		rownum += 1

#with open(path, "rb") as f:
#    filename = path.split("\\")[-1:][0]
#    encoded = b64encode(f.read())
#    image.attach_image(encoded, filename=filename)
#image.save()


#product = shopify.Product.find(2953308997)


