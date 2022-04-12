from django.db import models


class product(models.Model):
    product = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        if self.product:
            return f'{self.product} --> {self.price}'



# Create your models here.
