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
handle_ids = dict()

 #looping through csv
with open(csv_path,'rb') as f:	
 	rownum = 0
 	reader = csv.reader(f)
 	for row in reader:
 #		if rownum == 1:
 		if rownum >= 1:
 			row_list = []
 			for column in row:
 				row_list.append(column)
 			if row[0] not in handles:
 				handles[row[0]] = []
 				handles[row[0]].append(row_list)
 			else:
 				handles[row[0]].append(row_list)
 		rownum += 1
#Inserting products
for product in handles:
 	for variant in handles[product]:
 		if variant[1]:
 			print variant[42]
 		 	print variant[0]
 			new_product = shopify.Product()
 			new_product.handle = variant[0]
 			new_product.title = variant[1]
 			new_product.body_html = variant[2]
 			new_product.vendor = variant[3]
 			new_product.product_type = variant[4]
 			new_product.tags = variant[5]
# 			filename = __file__ + "\\..\\resource\\images\\" + variant[42]
 			filename = __file__ + "\\..\\resource\\images\\1.jpg"
 			print filename
 			image = shopify.Image()
 			with open(filename, "rb") as f:
 			    image.attach_image(f.read(), filename=filename)
 			new_product.images = [image]
 			print new_product.save()
 			v = shopify.Variant(dict(price=variant[19], option1=variant[8], image_id=new_product.images[0].id, product_id=new_product.id))
 			new_product.variants = [v]
 			success = new_product.save()
 			handle_ids[variant[0]] = new_product.id		
 			print success
#import variants
for product in handles:
 	for variant in handles[product]:
 		if not variant[1]:
 			print product
 			print variant[8]
# 			product_variant = shopify.Product.find(3360900293)
			if product not in handle_ids:
				continue
 			product_variant = shopify.Product.find(handle_ids[product])
 			filename = __file__ + "\\..\\resource\\images\\second.jpg"
 			print filename
 			new_image = shopify.Image()
 			with open(filename, "rb") as f:
 			    new_image.attach_image(f.read(), filename=filename)
 			product_variant.images.append(new_image)
 			print product_variant.save()
# 			product_variant = shopify.Product.find(3360799045)
 			product_variant = shopify.Product.find(handle_ids[product])
 			image_id = product_variant.images[len(product_variant.images)-1].id
 			v = shopify.Variant(dict(price=variant[19], option1=variant[8], image_id=image_id, product_id=product_variant.id ))
			product_variant.variants.append(v)
 			success = product_variant.save()
 			print success
