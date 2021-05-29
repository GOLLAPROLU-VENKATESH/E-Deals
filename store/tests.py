from django.test import TestCase
from .models.estore import Estore
from .models.category import Category
class EstoreTest(TestCase):
    def setUp(self):
        Estore.objects.create(name="ajio",count='3')
    def test_estore(self):
        name=Estore.objects.get(name="ajio")

class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(name="mobiles",count='5')
    def test_category(self):
        name=Category.objects.get(name="mobiles")