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
    
    data = Product.objects.all()
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
    
    result_list = sort_help(sorting, result)
    return_list = []
    for product in result_list:
        item = {
            "product_id" : product.product_id,
            "name" : product.name,
            "description" : product.description,
            "sales_data" : product.sales_data,
            "price" : round(float(product.price), 2),
            "picture" : product.picture,
            "features" : get_product_features(product.product_id) 
        }
        return_list.append(item)
        
    return return_list
    
def sort_help(sorting, list):
    result = []
    n = len(list)
    for i in range(n - 1):
        first = i
        for j in range(i+1, n):
            if (sorting == "price_low"):
                if list[j].price < list[first].price:
                    first = j
            if (sorting == "price_high"):
                if list[j].price > list[first].price:
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
        list[i], list[first] = list[first], list[i] 
        result.append(list[first])
        
    return result
            
        
