from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Group

class UserTests(APITestCase):    
    
    def test_user_list(self):
        # must be rejected without validation
        response = self.client.get('/api/users/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # must be success
        user = User.objects.create(username='user', email='user@example.com', password='user123', is_staff=True)
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/users/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        actual = response.data['results'][0]
        self.assertEqual(actual['username'], user.username)
        self.assertEqual(actual['email'], user.email)
