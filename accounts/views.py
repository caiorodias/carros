from django.contrib.auth.forms import AuthenticationForm # AutenticationForm vai pedir usuario e senha
from django.contrib.auth import authenticate, login, logout
from accounts.forms import CustomUserCreationForm # Form já pronto para crianção de user 
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST) # Esses if é só para criar validação
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password) # Autenticação do usuário
        if user is not None:
            login(request, user)
            return redirect('cars_list') # Se for validado ele loga e vai pra a lista de carros
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')
