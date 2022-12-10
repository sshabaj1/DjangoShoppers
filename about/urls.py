from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'about'

urlpatterns = [
    path('', views.about_page, name='about_page'),
     
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
