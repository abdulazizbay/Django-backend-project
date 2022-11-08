from django.db import models
from user.models import CustomUser as User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Category',null=True,blank=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass



    def __str__(self):
        return self.name
class Color(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Product(models.Model):
    choices = (
        ('Select a size','Select a size'),
        ('Small','Small'),
        ('Med','Med'),
        ('Large','Large'),
        ('Extra large','Extra large'),
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='Products')
    description = models.TextField()
    color = models.ManyToManyField(Color)
    size = models.CharField(max_length=20, choices=choices)
    quantity = models.IntegerField(default=1)
    reyting = models.FloatField(default=0)
    discount = models.FloatField(null =True,blank=True)

    @property
    def with_discount(self):
        if self.discount:
            return self.price*(1 - self.discount / 100)
        return self.price

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass


    def __str__(self):
        return self.name

class   Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,blank=True)
    total_price = models.FloatField(default=0)
    def __str__(self):
        return self.user.username



class  Cart_products(models.Model ):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)

    @property
    def summa(self):
        self.total = self.quantity * self.product.price
        self.save()
        return self.total

    @property
    def add(self):
        print('add')
        self.quantity+=1
        self.save()
        return self.quantity

    @property
    def sub(self):
        print('sub')
        self.quantity -= 1
        self.save()
        return self.quantity

    def __str__(self):
            return self.cart.user.username

class  Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username

class SaleHistory(models.Model):
    payment = (
        ('Humo', 'Humo'),
        ('Uzcard', 'Uzcard'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    payment_type = models.CharField(max_length=20, choices=payment)
    total_price = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username,self.time
