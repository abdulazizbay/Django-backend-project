from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from .models import Product
import json




def index(request):
    product  = Product.objects.all()
    categories = Category.objects.all().order_by('name')
    return render(request,'index.html',{'product':product,'categories':categories})

def search(request):
    if request.method == 'POST':
        key = request.POST['search']
        print(key)
        product = Product.objects.filter(Q(name__contains=key) |  Q(name__contains=key))
        print(product)
    return render(request,'search.html',{'product':set(product)})

def product_info(request,id):
    product = Product.objects.get(id=id)
    product_like = Product.objects.filter(category__product=product)
    return render(request,'product-extended.html',{'product':product,'product_like':product_like})

def product_by(request):
    data = json.loads(request.body)
    print(data['sort'])
    sort = data['sort']
    if sort=='reyting':
        products = Product.objects.all().order_by('-reyting')

    elif sort=='onsale':
        products = Product.objects.filter(quantity__isnull=False)

    pd = [{"id": p.id, "name": p.name, 'image': p.imageURL, 'price': p.price, 'discount': p.with_discount,"category": p.category.name,"reyting": p.reyting} for p in products]
    print(pd)
    return JsonResponse({"products":pd})

def cart(request):
    cart_products = Cart_products.objects.filter(cart__user = request.user)
    return render(request,'cart.html',{'products':cart_products,'total':cart_products.first().total})

#
# def add_to_cart(request):
#     data = json.loads(request.body)
#     id = data['id']
#     try:
#         cart = Cart.objects.get(user=request.user)
#     except:
#         cart = Cart.objects.create(user = request.user)
#     cart.product.add(Product.objects.get(id=id))
#     cart.save()
#     try:
#         cart_products = Cart_products.objects.get(cart_id=cart.id,product_id=id)
#         cart_products.add
#         cart_products.summa
#     except:
#
#         cart_products = Cart_products.objects.create(cart_id=cart.id,product_id = id)
#         cart_products.summa
#
#     prod = [{'id':p.id,'name':p.name,'price':p.price,'image':p.imageURL,'quantity':Cart_products.objects.get(cart_id=cart.id,product_id=p.id).quantity } for p in cart.product.all()]
#
#     return JsonResponse({'count':cart.product.all().count(),'product':prod})

def add_wishlist(request):
    id = json.loads(request.body)['id']
    try:
        user_wishlist = Wishlist.objects.get(user=request.user)
    except:
        user_wishlist = Wishlist.objects.create(user=request.user)
    product = Product.objects.get(id=id)
    if product in user_wishlist.product.all():
        user_wishlist.product.remove(product)
        return JsonResponse({'status':"Ok"})
    user_wishlist.product.add(product)
    return JsonResponse({'status':"Ok"})

def delete_wishlist(request):
    id = json.loads(request.body)['id']
    user_wishlist = Wishlist.objects.get(user=request.user)
    user_wishlist.product.remove(Product.objects.get(id=id))
    return JsonResponse({'status': "Ok"})



def wishlist(request):
    wishlist = Wishlist.objects.get(user=request.user)
    return render(request,'wishlist.html',{'wishlist':wishlist})

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def category(request,id):
    products_discount = Product.objects.filter(category_id=id, discount__isnull = False)
    products = Product.objects.filter(category_id=id, discount__isnull = True)
    categories = Category.objects.all().order_by('name')
    return render(request,'category-market.html',{'products':products,'categories':categories,'products_discount':products_discount})

def register(request):
    if request.method =='POST':
        #form = RegistrationForm(request.POST)
        #print("hello2")
        #if form.is_valid():
            #form.save()

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            User.objects.create_user(username=username,email=email,password=password1)

            user = authenticate(request,username = username,password=password1)
            print(user)
            if user:
                login(request,user)
                return redirect('index')
    return render(request,'register.html')

def loginfunc(request):
    if request.method =='POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username = username,password=password)

            if user:
                login(request,user)
                return redirect('index')

    return render(request,'login.html',{})

def logoutfunc(request):
    logout(request)
    return redirect('index')