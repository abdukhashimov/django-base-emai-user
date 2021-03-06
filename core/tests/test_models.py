from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_creating_user_with_email_successful(self):
        """Test that creating user with an email address is successful"""
        email = 'test@greatsoft.uz'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normilized(self):
        """Test the email for a new user is normilized"""
        email = 'test@GREATSOFT.UZ'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email(self):
        """Test to create a new user without email address"""
        email = None
        password = 'testpassword'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email='test@greatsoft.uz'
        password='testpassword'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)