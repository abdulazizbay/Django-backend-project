# #not working
# from store.models import Cart_products
# from django import template
#
# register = template.Library()
#
# @register.simple_tag
# def product_quantity(product_id, user):
#     print(Cart_products.objects.get(product_id=product_id))
#     return Cart_products.objects.get(cart__user=user ,product_id=product_id).quantity