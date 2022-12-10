from django.shortcuts import render , get_object_or_404
from .models import Product, Category
from shop.view_helper import ViewHelper



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)
    return render(request,
                'product/shop.html',
                {'category': category,
                'categories': categories,
                'products': products})




def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    featured_product_list = ViewHelper.return_featured_products()
    return render(request,
                  'product/shop-single.html',
                  {'product': product,
                  'featured_products': featured_product_list})