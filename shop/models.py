from django.db import models


class HeroPhoto(models.Model):
    slogan = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='media/hero',
                              blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)


class CollectionProduct(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/collection',
                              blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)



class FeaturedProduct(models.Model):
    name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    available = models.BooleanField(default=True)



class SaleProduct(models.Model):
    name = models.CharField(max_length=50)
    sale_date = models.DateField()
    sale_detail = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, db_index=True)
    sale_image = models.ImageField(upload_to='media/sale',
                              blank=True)



class PromoProduct(models.Model):
    name = models.CharField(max_length=50)
    promo_start_date = models.DateField()
    promo_end_date = models.DateField()
    promo_image = models.ImageField(upload_to='media/promo',
                              blank=True)