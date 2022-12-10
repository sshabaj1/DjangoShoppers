from django.shortcuts import render
from shop.view_helper import  ViewHelper




def about_page(request):
    promo_product = ViewHelper.return_promo_product()
    about_components = ViewHelper.return_about_components()
    return render(request, 'about/about.html',
                {'promo': promo_product,
                'about_components': about_components})