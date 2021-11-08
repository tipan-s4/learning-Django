from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Comprobamos la edad que introduce el usuario

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(15)
    ])
    email = models.EmailField()
    image = models.ImageField(default='user.png',blank=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 