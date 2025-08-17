from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class PostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    def test_post_list(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_create(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post-create'), {
            'title': 'New Post',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_post_update(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('post-update', kwargs={'pk': self.post.pk}),
            {'title': 'Updated Title', 'content': 'Updated Content'}
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')