from django.db import models
from django.contrib.auth.models import User
# importamos el modelo de usuario de django para añadirlo como dato del articulo
# Create your models here.
# creamos un Modelo para articulos
class Article(models.Model):
    # Añadimos los campos que conformaran un articulo
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 

    # Funcion que devuelve el titulo del articulo
    def __str__(self):
        return self.title

    # Funcion que devuelve las primeras 50 palabras del cuerpo del articulo
    def snippet(self):
        return self.body[:50]+'...'

# Creamos un modelo para los comentarios
class Comment(models.Model):
    body = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)