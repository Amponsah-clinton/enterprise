from django.contrib import admin
from .models import New_Product, Product, Employee, InvoiceItem, Invoice, UserProfile

admin.site.register(New_Product)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(InvoiceItem)
admin.site.register(Invoice)
admin.site.register(UserProfile)

