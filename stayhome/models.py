from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=30)
    category_in_Arabic = models.CharField(max_length=30)
    thumbnail = models.FileField(upload_to='media')

    def __str__(self):
        return self.category

class Service(models.Model):
    service_name = models.CharField(max_length=255)
    service_name_in_Arabic = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default=1)
    service_details_Arabic = models.CharField(max_length=1024)
    service_details_English = models.CharField(max_length=1024)
    website = models.CharField(max_length=255, null=True, blank=True)
    android = models.CharField(max_length=255, null=True, blank=True)
    iphone = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    logo = models.CharField(max_length=1024)
    
    #thumbnail = models.ImageField(upload_to = 'media')
    #description = RichTextField(max_length=255)

    def __str__(self):
        return self.service_name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Email_list(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

