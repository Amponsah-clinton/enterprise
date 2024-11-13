from django.db import models

class New_Product(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(New_Product, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    other_info = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.category.name} - ${self.price}"

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_address = models.TextField()
    products = models.ManyToManyField(Product, through='InvoiceItem')
    date = models.DateTimeField(auto_now_add=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    ghana_card_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

from django.db import models
import random
import string

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    user_id = models.CharField(max_length=10, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_unique_id()
        super().save(*args, **kwargs)
        
    def generate_unique_id(self):
        return ''.join(random.choices(string.digits, k=10))  # Generate random 10-digit ID

    def __str__(self):
        return self.username





























