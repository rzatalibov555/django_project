from django.contrib import admin

# Register your models here.

from pro_duct.models import Author, Product

# Register your models here.

admin.site.register([Author,Product])