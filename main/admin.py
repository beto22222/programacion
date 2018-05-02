from django.contrib import admin


from .models import Product,ProductImage,ProductCategory,User,Data

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory) 
admin.site.register(User)
admin.site.register(Data) 