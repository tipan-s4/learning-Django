from django import forms
from . import models

# Creamos el formulario para los articulos
class CreateArticle(forms.ModelForm):
    # La clase meta es necesaria para que django detecte que deseamos crear un formulario
    class Meta:
        model = models.Article
        fields = ['title','body','thumb']

class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Añade un comentario...'})
        }
        fields = ['body']
        # Añadimos un placeholder con el uso de los widgets 
        # (SE IMPORTAM EN LA PRIMERA FILA Y LA CLASE DEBE HEREDAR DE ELLA)