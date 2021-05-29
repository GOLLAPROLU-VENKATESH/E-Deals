from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, default='')
    user_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isEmailExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def isUserExists(self):
        if Customer.objects.filter(user_name=self.user_name):
            return True
        else:
            return False

    def isPhoneExists(self):
        if Customer.objects.filter(phone_number=self.phone_number):
            return True
        else:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


