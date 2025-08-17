from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-posts', kwargs={'slug': self.slug})

    @property
    def post_count(self):
        return self.posts.count()

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.title

    def get_tags_display(self):
        return ', '.join([tag.name for tag in self.tags.all()])

    def add_tags(self, tags_string):
        """
        Add tags to post from a comma-separated string
        """
        current_tags = set(self.tags.values_list('name', flat=True))
        new_tags = {tag.strip().lower() for tag in tags_string.split(',') if tag.strip()}
        
        # Remove tags that are not in the new set
        tags_to_remove = current_tags - new_tags
        if tags_to_remove:
            self.tags.remove(*Tag.objects.filter(name__in=tags_to_remove))
        
        # Add new tags
        for tag_name in new_tags:
            if tag_name not in current_tags:
                tag, created = Tag.objects.get_or_create(
                    name=tag_name,
                    defaults={'slug': tag_name.replace(' ', '-')}
                )
                self.tags.add(tag)

    def save(self, *args, **kwargs):
        # Create slug for new tags
        for tag in self.tags.all():
            if not tag.slug:
                tag.slug = tag.name.replace(' ', '-').lower()
                tag.save()
        super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})