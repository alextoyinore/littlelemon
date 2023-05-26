from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=5, inventory=25)
        self.assertEqual(item.__str__(), "IceCream : 5")
