# from django.conf.urls import url
from django.urls import path
from . import views

# Creamos las url
urlpatterns = [
    path('signup/',views.signup_view, name="signup"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('delete/',views.delete_view, name="delete"),
    path('profile/',views.profile_view, name="profile"),
    path('edit/',views.edit_view, name="edit"),
]