from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'date_joined')
    list_filter = ('role', 'date_joined')
    search_fields = ('user__username', 'phone_number')

# Register the custom user model and other models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)