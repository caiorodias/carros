
from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() # Igual SELECT * FROM CARS ( TRAZ TODOS OS DADOS DO BANCO DE DADOS)
    
    return render(
        request, 
        'cars.html', 
        {'cars': cars} #context
    ) #Renderiza uma requisição http e transforma numa response http
