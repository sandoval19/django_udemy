from django.test import TestCase
from django.contrib.auth import get_user_model
# allows to call urls of the project
from django.urls import reverse
# allows to make test requests to the app
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        # Creates connection to attempt request
        self.client = Client()
        # Create super user and login
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@aguacate.com',
            password='1234'
        )
        self.client.force_login(self.admin_user)
        # Create user and login
        self.user = get_user_model().objects.create_user(
            email='user@aguacate.com',
            password='9876',
            name='Test user'
        )

    def test_users_listed(self):
        """ Test that users are listed on user page"""
        # reverse url "app:url_to_requets"
        # notice, reverse allows to automatically update if the base url change
        url = reverse('admin:core_user_changelist')
        # request using http get method
        res = self.client.get(url)
        # this assertion looks for the value contain at the response obtained
        # also "checks" if the http response code is 200/400
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        # test that the web page renders ok
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
