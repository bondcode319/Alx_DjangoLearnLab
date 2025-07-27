from django.db import models
from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200),
    author = models.CharField(max_length=100),
    publication_year = models.IntegerField()




class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("can_view_all_posts", "Can view all blog posts"),
            ("can_create_posts", "Can create new blog posts"),
            ("can_edit_any_post", "Can edit any blog post"),
            ("can_delete_any_post", "Can delete any blog post"),
        ]

    def __str__(self):
        return self.title
    


class Command(BaseCommand):
    help = 'Creates default user groups and permissions'

    def handle(self, *args, **options):
        # Create groups
        viewer_group, _ = Group.objects.get_or_create(name='Viewers')
        editor_group, _ = Group.objects.get_or_create(name='Editors')
        admin_group, _ = Group.objects.get_or_create(name='Admins')

        # Get content type for Book model
        book_content_type = ContentType.objects.get_for_model(Book)
        
        # Get all permissions for Book model
        book_permissions = Permission.objects.filter(content_type=book_content_type)
        
        # Assign permissions to groups
        viewer_permissions = book_permissions.filter(codename__in=[
            'can_view_details',
        ])
        viewer_group.permissions.set(viewer_permissions)

        editor_permissions = book_permissions.filter(codename__in=[
            'can_view_details',
            'can_create_book',
            'can_edit_book',
            'can_view_restricted',
        ])
        editor_group.permissions.set(editor_permissions)

        # Admins get all permissions
        admin_group.permissions.set(book_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
        

from django.contrib.auth.models import UserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        
        if email:
            email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)   
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            
        return self.create_user(username, email, password, **extra_fields)