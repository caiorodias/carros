from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view, new_car_view #para puxar a função que está em views
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name = 'register'), #add
    path('login/', login_view, name= 'login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', cars_view, name= 'cars_list'), # Dando um nome para a url #add
    path('new_car/', new_car_view, name = 'new_car'), #add
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


