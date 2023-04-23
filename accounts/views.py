from django.contrib.auth.forms import UserCreationForm # Form já pronto para crianção de user
from django.shortcuts import render

def register_view(request):
    user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})