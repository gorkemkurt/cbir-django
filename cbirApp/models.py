from django.db import models


class Images(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, default='1')
    type = models.CharField(max_length=5)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    color_histogram = models.TextField()
    texture_histogram = models.TextField()

    class Meta:
        db_table = "images"


class DestImage(models.Model):
    name = models.CharField(max_length=50)
    dest_image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = "dest_images"
