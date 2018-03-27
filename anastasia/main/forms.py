from django import forms

class User(models.Model):

	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	id=models.IntegerField(primary_key=True)

	purchases = models.IntegerField(null=True)

	ip=models.CharField(max_length=200)
	first_name=models.CharField(max_length=200, null=True)
	last_name=models.CharField(max_length=200, null=True)

	email=models.CharField(max_length=200, null=True)

	
	def __str__(self):
		return self.email
