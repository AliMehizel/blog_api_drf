from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    model = User 
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Profile',
            {
                'fields':(
                    'avatar',
                    'slug',
                )
            }
        )
    )

admin.site.register(User, UserAdmin)


admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)