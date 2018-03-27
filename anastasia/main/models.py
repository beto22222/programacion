from django.db import models

# Create your models here.

class Product(models.Model):

	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	id=models.IntegerField(primary_key=True)
	punctuation=models.IntegerField()
	stock=models.IntegerField(null=True)

	price = models.DecimalField(max_digits=8, decimal_places=2)

	name=models.CharField(max_length=200)
	description_es=models.TextField(max_length=400,null=True)
	description_en=models.TextField(max_length=400,null=True)

	slug=models.SlugField()

	def __str__(self):
		return self.name

class ProductImage(models.Model):
	
	product=models.ForeignKey('main.Product',on_delete=models.CASCADE,related_name='images')
	image=models.ImageField()


	def __str__(self):
		return self.image.url


class ProductCategory(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)


	name=models.CharField(max_length=200)

	slug=models.SlugField()


	def __str__(self):
		return self.name


