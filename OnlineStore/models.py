from django.db import models


class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    Description = models.CharField(max_length=20)
   