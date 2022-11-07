from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('product_info/<int:id>/',product_info,name='product_info'),
    path('product_by/',product_by,name = 'product_by'),

    path('search/',search,name = 'search'),
    # path('add_to_cart/',add_to_cart,name = 'add_to_cart'),
    path('cart/',cart,name='cart'),
    path('add_wishlist/',add_wishlist,name='add_wishlist'),
    path('delete_wishlist/',delete_wishlist,name='delete_wishlist'),

    path('wishlist/',wishlist,name='wishlist'),
    path('category/<int:id>/',category,name='category'),
    path('contact/',contact,name='contact'),
    path('checkout/',checkout,name='checkout'),

    path('login/',loginfunc,name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutfunc, name='logout'),

]