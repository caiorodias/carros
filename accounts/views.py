from accounts.forms import CustomUserCreationForm # Form já pronto para crianção de user
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('cars_list')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})