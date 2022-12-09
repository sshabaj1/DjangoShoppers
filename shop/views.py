from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import HeroProduct, CollectionProduct , FeaturedProduct, SaleProduct, PromoProduct
from .view_helper import ViewHelper


class LandingPageView(generic.TemplateView):
    template_name = 'index.html'


def landind_page_view(request):

    
    hero_product_list = HeroProduct.objects.all()
    hero_product = ViewHelper.return_available_product(hero_product_list)


    collectin_product_list = CollectionProduct.objects.all()
    collectin_products_available = ViewHelper.return_available_product_list(collectin_product_list)

    featured_product_list = FeaturedProduct.objects.all()
    featured_products_available = ViewHelper.return_available_product_list(featured_product_list)


    sale_product_list = SaleProduct.objects.all()
    sale_product = ViewHelper.return_available_product(sale_product_list)

    promo_product_list = PromoProduct.objects.all()
    promo_product = ViewHelper.return_available_product(promo_product_list)


    return render(request,
                  'index.html',
                  {'hero': hero_product,
                   'collections': collectin_products_available,
                   'featured_list': featured_products_available,
                   'sale': sale_product,
                   'promo': promo_product})

