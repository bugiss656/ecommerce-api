from django.test import TestCase
from .models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('customers:register')

def create_user(**params):
        return User.objects.create_user(**params)


class UserTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'email': 'testuser1@mail.com',
            'password': 'testuser1111',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '111222333'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=payload['email'])
        self.assertTrue(user)

    def test_user_password_correct(self):
        payload = {
            'email': 'testuser2@mail.com',
            'password': 'testuser2222',
            'first_name': 'Tony',
            'last_name': 'Hawk',
            'phone': '333222111'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        user = User.objects.get(email=payload['email'])

        self.assertTrue(user.check_password(payload['password']))

    def test_user_already_exists_error(self):
        payload = {
            'email': 'testuser1@mail.com',
            'password': 'testuser1111',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '111222333'
        }
        
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_length_error(self):
        payload = {
            'email': 'testuser1@mail.com',
            'password': 'test',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '111222333'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user)
