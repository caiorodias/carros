
from django.shortcuts import render
from cars.models import Car

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
