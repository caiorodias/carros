
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all().order_by('brand')
    #order_by serve para ordenar se colocar('-brand') vai mostrar em ordem invertida
    #O usuário está aqui, se ele fizer alguma requisição, ele vai para o if e muda o valor do cars para o search.

    #print(request.GET.get('search')) #Para receber a requisição que o user ta fazendo na url.
    #print(request.GET)
    search = request.GET.get('search')

    if search: #Se search tem algo, se for nula não cai no if.
        cars = cars.filter(model__icontains = search) # Igual SELECT * FROM CARS ( TRAZ TODOS OS DADOS DO BANCO DE DADOS)
    #cars= Car.objects.filter(brand__name =  'Fiat') #brand é pesquisado por numero pq o brand estão por primary key // mas se colocar o brand__name pode pesquisar pelo nome
    #cars = Car.objects.filter(model__contains = '1.8') # O __contains server para buscar qualquer um que contem aquele pedaço de string. NÃO É CASE SENSITIVE
    # o cars dentro do if so está cars.filter pq a variavel já está la em cima com Car.object, senão seria Car.objects.filter()


    return render(
        request, 
        'cars.html', 
        {'cars': cars} #context
    ) #Renderiza uma requisição http e transforma numa response http

def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES) # Request.POST vai ter todos os dados que o usuário enviou e o .FILES é para o arquivo de imagem
        if new_car_form.is_valid(): # Estão válidos?
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form}) # Context
