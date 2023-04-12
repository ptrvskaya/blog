from django.test import TestCase, Client
from .models import Post
from django.contrib.auth.models import User, Group
from django.urls import reverse


class TestViewsBlog(TestCase):
    def setUp(self):
        Post.objects.create(title="one two three", description="some text", topic="E", content="test test test test", picture="file_one.jpg")
        Post.objects.create(title="testing", description="some text 4 test", topic="T", content="test test test test", picture="file_two.jpg")
        Post.objects.create(title="Test post", description="some more text", topic="S", content="test test test test", picture="file_three.jpg")
    
    def test_main_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Malish's test blog",
                    response.content.decode())

    def test_AllPosts_view(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Malish's test blog",
                    response.content.decode())

    def test_OnePost_view(self):
        self.post = Post.objects.create(title="one two three four", description="text text text", topic="E", content="test test test test", picture="file_4.jpg")
        url = reverse('one_post', kwargs={'slug': self.post.slug})
        response = self.client.get(url)        
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)

    def test_anonymous_user(self):
        client = Client()
        client.logout()
        response = client.get('/posts/new_post/')
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/accounts/login/?next=/posts/new_post/')  


class TestAuthentication(TestCase):
    def setUp(self):
        self.client = Client()
        self.group = Group.objects.create(name='Author')
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'YQG9yC787E0')

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'YQG9yC787E0'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main_page'))


    def test_registration(self):
        data = {'username': 'newtestuser', 'password1': '7M$y92yJc4&U', 'password2': '7M$y92yJc4&U'}
        response = self.client.post(reverse('registration'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main_page'))
        self.assertTrue(User.objects.filter(username='newtestuser').exists())


