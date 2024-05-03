from django.db import models

# Create your models here.
class Books(models.Model):

    title=models.CharField(max_length=500)
    author=models.CharField(max_length=500)
    description=models.CharField(max_length=5000)
    price=models.IntegerField()
    Categray=models.CharField(max_length=5000)
    slug=models.SlugField()
    img=models.ImageField(upload_to='photo')
    pages=models.IntegerField()