from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ContactForm, ProductModelForm
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {
            'products': products}
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, "Done.")
            form = ContactForm()
        else:
            messages.error(request, "Error")
            
    context = {
            'form': form
            }
    return render(request, 'contact.html', context)


def product(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProductModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product saved.')

                form = ProductModelForm()
            else:
                messages.error(request, 'Error to save')
        else:
            form = ProductModelForm()
        context = {
                'form': form
                }
        return render(request, 'product.html', context)
    
    return redirect('index')
