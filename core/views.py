from django.shortcuts import render
from product.models import Product
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def landing_page(request):
    if request.method == "POST":
        return redirect(reverse('core:home'))
    return render(request, 'core/landing.html')

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    context = {
        'newest_products': newest_products,
    }
    return render(request, 'core/frontpage.html', context)


def contactpage(request):
    return render(request, 'core/contact.html')

def landing(request):
    return render(request, 'landing.html')