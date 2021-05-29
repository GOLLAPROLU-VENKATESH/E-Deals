from django.db import models

class ContactUs(models.Model):
    user_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    query =models.TextField(max_length=2000)
    img = models.ImageField(upload_to='uploads/contact/', blank=True)

    def register(self):
        self.save()