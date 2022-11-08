from .models import Cart, Category,Cart_products

def context_pro(request):
    product1 = Cart.objects.get(user=request.user).product.all()
    category = Category.objects.all()

    context={
        'cart_prod':product1,
        'category':category,
        'total': sum(Cart_products.objects.filter(card__user=request.user).values_list('total',flat=True)),
        'count':product1.count(),

    }
    return context