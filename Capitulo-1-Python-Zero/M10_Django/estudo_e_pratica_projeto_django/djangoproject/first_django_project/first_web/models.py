from django.contrib.auth.models import User #para reconhecer o usuario (explicação ruim)
from django.db import models

# Create your models here.
class Post(models.Model): #criamos uma classe para dar inicio a criação dos nossos post
    title = models.CharField(max_length=255) #max_leng limita o numero maximo de caracteres
    sumary = models.CharField(max_length=255) #ussa mesma estrutura que o titulo, descobrir como usar models e seus atributos CharField, Text...
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    created_date = models.DateField(auto_now_add = True)
