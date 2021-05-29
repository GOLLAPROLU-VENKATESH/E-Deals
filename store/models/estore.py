from django.db import models

class Estore(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_estores():
        return Estore.objects.all()
    @staticmethod
    def get_estore_by_object(estore_id):
        return Estore.objects.filter(id=estore_id)