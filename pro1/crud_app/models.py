from django.db import models

class Grocery(models.Model):
    product_name=models.CharField(max_length=20)
    product_quan=models.IntegerField()
