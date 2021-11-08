from product.models import Product, Features
from product.errors import ProductIdError
from user.errors import InputError
from user.models import Admin
from product.products import get_product_features

def get_search_result(email, search, sorting):
    if sorting != "price_low" and sorting != "price_high" and sorting != "best_sell" and sorting != "a_to_z" and sorting != "z_to_a":
        raise InputError("The sorting is invalid")
    
    if search == "":
        raise InputError("The search word in empty")
    
    data = Product.objects.filter()
    result = []
    for product in data:
        # if the search word in the product name or desription
        if search in product.name or search in product.description:
            result.append(product)
            continue

        # if the search word in the product feature
        features = Features.objects.filter(product_id = product.product_id)
        for feature in features:
            if search in feature.feature:
                result.append(product)
                break
    
    result_list = sort_help(sorting, result)
    return_list = []
    for product in result_list:
        item = {
            "product_id" : product.product_id,
            "name" : product.name,
            "description" : product.description[:30],
            "sales_data" : product.sales_data,
            "price" : round(float(product.price), 2),
            "picture" : product.picture,
            "features" : get_product_features(product.product_id) 
        }
        return_list.append(item)
        
    return return_list
    
def sort_help(sorting, list):
    result = []
    return recursion_help(result, list, sorting)
            
def recursion_help(result, list, sorting):
    if len(list) == 0:
        return result
    first = 0
    for j in range(0, len(list)):
        if (sorting == "price_low"):
            if list[j].price < list[first].price:
                first = j
        if (sorting == "price_high"):
            if list[j].price > list[first].price:
                print(11)
                first = j
        if (sorting == "best_sell"):
            if list[j].sales_data > list[first].sales_data:
                first = j
        if (sorting == "a_to_z"):
            if list[j].name < list[first].name:
                first = j
        if (sorting == "z_to_a"):
            if list[j].name > list[first].name:
                first = j

    result.append(list[first])
    list.remove(list[first])
    return recursion_help(result, list, sorting)