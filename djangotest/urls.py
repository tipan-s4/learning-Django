from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
# Al haber importado ya las views de el mismo directorio cambiamos el nombre para evitar confucion
from articles import views as article_views


# Incluimos las urls de nuestras apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('articles.urls')),
    path('about/', views.about),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
