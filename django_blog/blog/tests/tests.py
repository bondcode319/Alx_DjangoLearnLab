from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from django.core.files.uploadedfile import SimpleUploadedFile

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('signup')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.test_user = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!'
        }

    def test_signup_view(self):
        # Test GET request
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

        # Test POST request with valid data
        response = self.client.post(self.register_url, self.test_user)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login_view(self):
        # Create a user
        User.objects.create_user(username='testuser', password='TestPass123!')
        
        # Test login with correct credentials
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'TestPass123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_profile_view(self):
        # Create and login user
        user = User.objects.create_user(username='testuser', password='TestPass123!')
        self.client.login(username='testuser', password='TestPass123!')

        # Test GET request
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')

        # Test profile update
        response = self.client.post(self.profile_url, {
            'username': 'testuser_updated',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 302)
        updated_user = User.objects.get(pk=user.pk)
        self.assertEqual(updated_user.email, 'updated@example.com')

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass123!'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_creation(self):
        self.assertEqual(str(self.profile), 'testuser Profile')
        self.assertEqual(self.profile.user.username, 'testuser')
