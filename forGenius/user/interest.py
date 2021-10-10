from user.models import User
from user.errors import InputError

# def user_interest(interest_list):
#     try:
#         product_query = Product.objects.get(pk=product_id)
#     except Product.DoesNotExist:
#         raise ProductIdError("This product does not exist")

#     info = {
#             "name" : product_query.name,
#             "description" : product_query.description,
#             "warranty" : product_query.warranty,
#             "delivery_date" : product_query.delivery_date
#         } 
#     return info