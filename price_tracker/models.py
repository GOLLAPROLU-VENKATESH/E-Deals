import requests
from django.db import models

# Create your models here.
from django.db import models
from .utils import get_link_data


# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000)
    current_price = models.FloatField(blank=True)
    target_price = models.FloatField(default=0)
    price_diff = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    nemail =models.BooleanField(default=False)
    customer =models.CharField(max_length=50, default='')
    min_target = models.FloatField(default=0)
    max_target = models.FloatField(default=0)



    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('price_diff', '-created')

    def register(self):
        self.save()

    def update(self):
        self.update()

    def save(self, *args, **kwargs):
        name, price,error = get_link_data(self.url)
        target_price = self.target_price
        if self.current_price:
            if price != target_price:
                diff = price - target_price
                self.price_diff = round(diff, 2)
            else:
                self.price_diff = 0
        self.name = name
        self.current_price = price
        super().save(*args, *kwargs)
# celery -A ec3 beat -l info
# celery -A ec3 worker -l info
#celery -A proj purge