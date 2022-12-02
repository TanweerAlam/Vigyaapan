from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'gender', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'gender',
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('gender',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)