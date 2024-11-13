from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('products/', views.product_list_view, name='product_list'),
    path('new-product/', views.new_product, name='new_product'),
    path('generate-invoice/', views.generate_invoice, name='generate_invoice'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('employee-list/', views.employee_list, name='employee_list'),
    path('emp/', views.emp, name='emp'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'), 
      path('save-invoice/', views.save_invoice, name='save_invoice'),




]