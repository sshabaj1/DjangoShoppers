from django.shortcuts import render , get_object_or_404
from .models import Product, Category



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)
    return render(request,
                'shop.html',
                {'category': category,
                'categories': categories,
                'products': products})
