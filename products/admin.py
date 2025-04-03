from django.contrib import admin
from .models import Product

admin.site.register(Product)

from .models import BlockList
admin.site.register(BlockList)
