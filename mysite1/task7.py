from multiprocessing.shared_memory import ShareableList
from home.models import Product

#NOTE: click enter after each line please
#inserting a new record in the Product Model

python manage.py shell #takes the cmd to the ORM mode
from mysite1.task7 import Product #to import attributes of Product model to task7.py
x= Product(product_name = 'MagElle herbal', product_category = 'skin booster', product_price = 500) #we are assigning new records to the Product model
x.save() #this is to save the command to the Product model

#getting all the records in the Product table
#after following steps 7 and 8 above
Product.objects.all() #this command gets all the saved records in the Product table

#To filter Products by their name
Product.objects.filter(product_name= 'MagElle herbal')

#Getting a single record from the product table
Product.objects.get(id=2) #all records have their unique id

#to change a product price
x= Product.objects.get(product_price =1000) #this locates the product with price of 1000
x.product_price = 1700 #this command changes the price from 1000 to 1700
x.save()

