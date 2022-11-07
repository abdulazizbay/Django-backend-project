# from .models import Cart, Category
#
# def context_pro(request):
#     product1 = Cart.objects.get(user=request.user).product.all()
#     category = Category.objects.all()
#     total = sum(product1.values_list('price',flat=True))
#     context={
#         'cart_prod':product1,
#         'category':category,
#         'total':total,
#         'count':product1.count(),
#
#     }
#     return context