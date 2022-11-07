from django.db import models
from django.contrib.auth.models import AbstractUser
import random

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    is_verify = models.BooleanField(default=False)

    @property
    def is_admin(self):
        return self.is_superuser

class Code(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number = models.CharField(max_length=5,blank=True)

    def __str__(self):
        return f"{self.user.username} | {self.number}"

    def save(self,*args,** kwargs):
        number_list = [x for x in range(10)]
        code_items = ''
        for i in range(5):
            num = random.choice(number_list)
            code_items += str(num)
        self.number = code_items
        super().save(*args,** kwargs)


