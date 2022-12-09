class ViewHelper():

    def return_available_product(product_list):
        for product in product_list:
            if product.available == True:
                return product


    def return_available_product_list(product_list):
        list_to_return = []
        for product in product_list:
            if product.available == True:
                list_to_return.append(product)

        return list_to_return