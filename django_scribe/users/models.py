from django.db import models
from Books.models import Book
# from Books.models import Book
# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=120)
    contact = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank= True)
    photo = models.ImageField(null= True, blank=True)
    wishlist = models.


    def __str__(self) -> str:
        return self.name
    
    # @property
    # def rating(self):
    #     pass