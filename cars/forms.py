from django import forms
from cars.models import Brand

class CarForm(forms.Form): #forms.Form já é um formulário pronto do django.
    model = forms.CharField(max_length= 200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #Puxando as marcas pelo query sets.
    factory_year = forms.IntegerField() 
    model_year = forms.IntegerField() #ano
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField() # Repete os mesmos campos do modelo.