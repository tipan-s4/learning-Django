from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# importamos un decorador propio de django para comprobar que el usuario esta logeado
from . import forms
from django.contrib.auth import get_user_model
# Para obtener todos los usuarios
from django.utils import timezone
# hora 
from accounts.models import Profile
# Importamos los perfiles los usuarios


# Create your views here.

# Mostramos los articulos
def article_list(request):
    articles =  Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})


# Mostramos los detalles de los articulos
def article_detail(request, pk):
    # Obtenemos el articulo al que añadir los comentarios
    # Obtenemos los comentarios que proveengan de dicho articulo
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.all().filter(article=article) 
    profiles = Profile.objects.all() 
    # profile = get_object_or_404(Profile,username=request.user)
    if request.method == 'POST':
        # Si el metodo es post comprobamos que el usuario tiene un perfil
        profile = Profile.objects.all().filter(username=request.user) 
        if profile:
            form = forms.CreateComment(request.POST)
            if form.is_valid():
                # Añadimos los campos necesarios al comentario y lo guardamos
                comment = form.save(commit=False)
                comment.date = timezone.now()
                comment.author = request.user
                comment.article = article
                comment.save()
                # Redirigimos a la pagina del articulo
                return redirect(f'/article/{pk}/')
        else:
            return redirect('/accounts/profile/')
    else:
        # Creamos un formulario de comentario
        form = forms.CreateComment()
    # Redirigimos con los datos del articulo, el formualrio para crear un nuevo comentario y los cometarios del articulo
    return render(request, 'articles/article_detail.html',{'article':article, 'form':form, 'comments':comments, 'profiles':profiles})

# Comprobamos que se ha iniciado sesion para poder crear un articulo
@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})


# Comprobamos que el usuario ha iniciado sesion para poder editar un articulo
@login_required(login_url="/accounts/login/")
def article_edit(request,pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user
    author = article.author
    # Comprobamos que el usuario logeado es el mismo que el autor del articulo
    if user == author:
        if request.method == 'POST':
            form = forms.CreateArticle(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit = False)
                article.date = timezone.now()
                article.save()
                return redirect('article_detail', pk=article.pk)
        else:
            article = forms.CreateArticle()
        return render(request, 'articles/article_edit.html',{'article':article})
    else:
        return render(request, 'articles/article_edit.html')


# Borramos el articulo
def article_delete(request,pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('/')

# Obtenemos todos los usuarios en nuestra base de datos
def article_authors(request):
    User = get_user_model()
    authors = User.objects.all()
    return render(request, 'articles/authors.html',{'authors':authors})

# Obtenemos los articulos de un usuario determinado
def article_byauthor(request, id):
    articles = Article.objects.all().filter(author=id) 
    return render(request,'articles/byAuthor.html',{'articles':articles})

# Borramos el comentario
def comment_delete(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('/')