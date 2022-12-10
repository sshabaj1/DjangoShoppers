from django.shortcuts import render
from shop.view_helper import  ViewHelper




def about_page(request):
    promo_product = ViewHelper.return_promo_product()
    return render(request, 'about/about.html',
                {'promo': promo_product})