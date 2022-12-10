from django.shortcuts import render
from shop.view_helper import ViewHelper
from .models import Location




def contact_page(request):
    promo_product = ViewHelper.return_promo_product()
    locations = Location.objects.all()

    return render(request, 'contact/contact.html',
                {'promo':promo_product,
                'locations': locations})