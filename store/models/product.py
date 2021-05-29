from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .category import Category
from .estore import Estore


class Product(models.Model):
    name = models.CharField(max_length=100)
    seller_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, validators=[
        MinValueValidator(0), MaxValueValidator(5)])
    mrp = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    description = models.TextField(max_length=500)
    img_1 = models.ImageField(upload_to='uploads/product/')
    img_2 = models.ImageField(upload_to='uploads/product/')
    start_time = models.DateTimeField(blank=True)
    End_time = models.DateTimeField(blank=True)
    uploaded_time = models.DateTimeField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    estore = models.ForeignKey(Estore, on_delete=models.CASCADE, default=1)
    product_url = models.URLField(max_length=500, default="localhost:8000")

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.order_by('-uploaded_time')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_all_categories_by_id(category_id):
        if category_id:
            cap = Category.get_category_by_object(category_id)
            for o in cap:
                o.count = o.count + 1
                o.save()
            return Product.objects.filter(category_id=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_estore_id(estore_id):
        if estore_id:
            esp=Estore.get_estore_by_object(estore_id)
            for o in esp:
                o.count=o.count+1
                o.save()
            return Product.objects.filter(estore_id=estore_id)
        else:
            return Product.get_all_products()
