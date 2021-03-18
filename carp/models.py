from django.db import models

# Create your models here.

class book(models.Model):
    Title= models.CharField(max_length=50)
    description= models.TextField(max_length=400)
    category = models.CharField(max_length=50, null=True)
    File= models.FileField(blank=True)
    imageFile= models.ImageField(blank=True)

    def __str__(self):
        return self.Title

class activity(models.Model):
    event = models.CharField(max_length=50)
    description= models.TextField(max_length=400)
    Date= models.DateField
    image= models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.event


class notification(models.Model):
    name = models.CharField(max_length=50)
    Link = models.URLField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)


    def __str__(self):
        return self.name

class album(models.Model):
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.description
