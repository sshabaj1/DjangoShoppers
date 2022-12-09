from django.db import models


class HeroProduct(models.Model):
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='hero',
                              blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)


class CollectionProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='collection',
                              blank=True)
    slug = models.SlugField(max_length=200, db_index=True)
    available = models.BooleanField(default=True)



class FeaturedProduct(models.Model):
    name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='feature',
                              blank=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)



class SaleProduct(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    detail = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='sale',
                              blank=True)
    available = models.BooleanField(default=True)


class PromoProduct(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='promo',
                              blank=True)
    available = models.BooleanField(default=True)