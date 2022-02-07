from django.db import models
from django.conf import settings
# Create your models here.

class MyProducts(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.FloatField()
    User= settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def create(self):
        self.save()
    @property
    def all_fields(self):
        return '{}{}{}'.format(self.name, self.desc, self.price, self.user, self.img)
    
    def __str__(self):
        return self.all_fields

class TodoListItem(models.Model):
    content = models.TextField()
    def __str__(self):
        return self.content

class CustomProductsItem(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.FloatField()
    seller = models.CharField(max_length=255)

    def create(self):
        self.save()
    @property
    def all_fields(self):
        return '{}{}{}'.format(self.name, self.desc, self.price, self.seller)
    
    def __str__(self):
        return self.all_fields

