from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
