from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'WIMEX'

class ProductAdmin(admin.StackedInline):
    model = AdditionalInfo

class ImageAdmin(admin.TabularInline):
    model = Image

class ProductInlineInfoAdmin(admin.ModelAdmin):
    inlines = (ProductAdmin, ImageAdmin)

admin.site.register(Product, ProductInlineInfoAdmin)