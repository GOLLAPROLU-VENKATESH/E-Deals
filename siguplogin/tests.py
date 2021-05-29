from django.test import TestCase
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(first_name="venkatesh",last_name="venky",user_name="venkatesh1501",phone_number="6549873210",email="venkyvenkatesh5408@gmail.com",password="venkatesh")

    def test_customer(self):
        name=Customer.objects.get(first_name="venkatesh")
        print(name)


