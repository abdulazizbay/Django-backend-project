from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class Admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if len(str(obj.password)) < 20:
            obj.set_password(obj.password)
        super(Admin, self).save_model(request, obj, form, change)

admin.site.register(Code)
