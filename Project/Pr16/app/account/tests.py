from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import RegisterForm

# Create your tests here.
class TestCaseViewAccount(TestCase):

    def setUp(self) -> None:
        self.form_data ={
            'username' : 'Nikitin',
            'email' : 'Bogdan@mail.ru',
            'password1' : 'BogdanBogdan',
            'password2' : 'BogdanBogdan',
        }
    
    def test_register_view(self):

        RegisterForm(data=self.form_data)
        self.client.post(reverse('register'), data=self.form_data)
        user = User.objects.filter(username=self.form_data['username']).exists()
        self.assertTrue(user)
