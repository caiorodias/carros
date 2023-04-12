from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view #para puxar a função que está em views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view, name= 'cars_list'), # Dando um nome para a url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


