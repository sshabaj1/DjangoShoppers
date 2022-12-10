from .models import HeroProduct, CollectionProduct , FeaturedProduct, SaleProduct, PromoProduct


class ViewHelper():




    def filter_available_product(product_list):
        for product in product_list:
            if product.available == True:
                return product



    def filter_available_list(product_list):
        list_to_return = []
        for product in product_list:
            if product.available == True:
                list_to_return.append(product)

        return list_to_return


    def return_hero_product():
        hero_product_list = HeroProduct.objects.all()
        hero_product = ViewHelper.filter_available_product(hero_product_list)
        return hero_product


    def return_collection_products():
        collectin_product_list = CollectionProduct.objects.all()
        collectin_products_available = ViewHelper.filter_available_list(collectin_product_list)
        return collectin_products_available

    
    def return_sale_product():
        sale_product_list = SaleProduct.objects.all()
        sale_product = ViewHelper.filter_available_product(sale_product_list)
        return sale_product


    def return_featured_products():
        featured_product_list = FeaturedProduct.objects.all()
        featured_products_available = ViewHelper.filter_available_list(featured_product_list)
        return featured_products_available


    def return_promo_product():
        promo_product_list = PromoProduct.objects.all()
        promo_product = ViewHelper.filter_available_product(promo_product_list)
        return promo_product

    