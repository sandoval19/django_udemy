from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@aguacate.com'
        psw = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=psw
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(psw))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = 'test@AGUACATE.COM'
        user = get_user_model().objects.create_user(email,'test1234')

        self.assertEqual(user.email,email.lower())