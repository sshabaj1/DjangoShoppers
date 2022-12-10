from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list-page'),
     path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
