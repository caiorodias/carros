
from django.shortcuts import render

def cars_view(request):
    return render(
        request, 
        'cars.html', 
        {'cars': {'model': 'Astra 2.0'}} #context
        ) #Renderiza uma requisição http e transforma numa response http
