from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# Registramos el modelo de articulo y el de comentario
# Nota: recordar hacer las migraciones siempre que modifiquemos los modelos
admin.site.register(Article)
admin.site.register(Comment)
