from django.contrib import admin
from .models import User



class UserModelAdmin(admin.ModelAdmin):
    '''
        Encapsulate all admin options and functionality for a given model.
    '''
    list_display = [
        "email", "date_joined",
        "is_active", "is_staff"
    ]
    save_on_top = True



admin.site.register(User, UserModelAdmin)