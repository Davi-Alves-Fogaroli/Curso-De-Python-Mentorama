from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post_um(models.Model):
    title = models.CharField(max_length = 255)
    sumary = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    created_date = models.DateField(auto_now_add = True)

class Language(models.Model):
    name = models.CharField(max_length = 20)
    creator = models.CharField(max_length=20)
    paradigm = models.CharField(max_length=20)
    date_created = models.DateField()

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name