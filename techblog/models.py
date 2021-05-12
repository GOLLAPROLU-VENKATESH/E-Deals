from django.db import models


class Techblog(models.Model):
    heading = models.CharField(max_length=100)
    subheading1 = models.CharField(max_length=500)
    subheading2 = models.CharField(max_length=500, blank=True)
    subheading3 = models.CharField(max_length=500, blank=True)
    para1 = models.TextField(max_length=200)
    para2 = models.TextField(max_length=1000, blank=True)
    para3 = models.TextField(max_length=1000, blank=True)
    img_1 = models.ImageField(upload_to='uploads/blog/')
    img_2 = models.ImageField(upload_to='uploads/blog/', blank=True)
    img_3 = models.ImageField(upload_to='uploads/blog/', blank=True)
    video = models.URLField(max_length=1000,default='null')
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    @staticmethod
    def get_all_techblog():
        return Techblog.objects.order_by('-uploaded_time')

    @staticmethod
    def get_blog_by_id(bid):
        if bid:
            return Techblog.objects.filter(id=bid)
        else:
            return Techblog.objects.order_by('-uploaded_time')