from django.urls import path
# from django.conf.urls import url
from . import views


# Creamos las url
# En algunas url pasamos el pk que es una propiedad unica que usa django
urlpatterns = [
    path('', views.article_list, name='home'),
    path('create/',views.article_create, name='create'),
    path('Authors/',views.article_authors, name='autor'),
    path('byAuthor/<int:id>/',views.article_byauthor, name='byAuthor'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/remove/', views.article_delete, name='article_delete'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('comment/<int:pk>/remove/', views.comment_delete, name='comment_delete'),
]
