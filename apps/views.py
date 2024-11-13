from django.shortcuts import render, redirect
from .forms import ProductForm, NewProductForm
from .models import Product, New_Product

def home(request):
    return render(request, 'home.html')

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm()
    return render(request, 'products.html', {'form': form})


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def new_product(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = NewProductForm()
    return render(request, 'new_product.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Invoice, InvoiceItem, Product
from .forms import InvoiceForm, InvoiceItemForm
from django.forms import formset_factory

def generate_invoice(request):
    # Retrieve all products to display in the form
    products = Product.objects.all()

    # Dynamically generate the InvoiceItem formset
    InvoiceItemFormSet = formset_factory(InvoiceItemForm, extra=1)

    if request.method == 'POST':
        # Instantiate the forms with POST data
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST, prefix='items')

        if form.is_valid() and formset.is_valid():
            # Save the invoice form and retrieve the invoice instance
            invoice = form.save()

            # Loop through the formset and save each InvoiceItem
            for item_form in formset:
                if item_form.cleaned_data:
                    invoice_item = item_form.save(commit=False)
                    invoice_item.invoice = invoice
                    invoice_item.save()

            # Redirect to a success page after the invoice is saved
            return redirect('invoice_success')  # Make sure 'invoice_success' is a valid URL name
    else:
        # For GET request, initialize the forms
        form = InvoiceForm()
        formset = InvoiceItemFormSet(prefix='items')

    # Passing the products and the formset context for dynamic pricing and product selection
    context = {
        'products': products,
        'form': form,
        'formset': formset,
    }
    return render(request, 'generate_invoice.html', context)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Invoice, InvoiceItem  # Assuming you have these models defined

@csrf_exempt
def save_invoice(request):
    if request.method == "POST":
        # Retrieve data from the request
        customer_name = request.POST.get("customer_name")
        customer_phone = request.POST.get("customer_phone")
        customer_address = request.POST.get("customer_address")
        items = request.POST.getlist("items[]")
        grand_total = request.POST.get("grand_total")

        # Save the invoice
        invoice = Invoice.objects.create(
            customer_name=customer_name,
            customer_phone=customer_phone,
            customer_address=customer_address,
            total=grand_total
        )

        # Save each invoice item
        for item in items:
            product_name = item["product_name"]
            quantity = item["quantity"]
            price = item["price"]
            total = item["total"]
            InvoiceItem.objects.create(
                invoice=invoice,
                product_name=product_name,
                quantity=quantity,
                price=price,
                total=total
            )

        return JsonResponse({"status": "success", "message": "Invoice saved successfully."})





from .models import Employee
from .forms import EmployeeForm

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def emp(request):
    return render(request, 'emp.html')


from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import UserProfile
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            
            try:
                user = UserProfile.objects.get(user_id=user_id, password=password)
                messages.success(request, 'Login successful.')
                return redirect('home')  
            except UserProfile.DoesNotExist:
                messages.error(request, 'Invalid ID or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

























