from django.db import models

# Create your models here.
class BookList(models.Model):
    name= models.CharField(max_length=50,blank=True,null=True)
    price=models.IntegerField()
    author=models.CharField(max_length=50, blank= True , null= True)