from django import forms
from cars.models import Brand, Car

# Forma correta usando o ModelForm

class CarModelForm(forms.ModelForm): # Isso substitui tudo isso comentado de cima, pq liga diretamente com o model Car
    class Meta:
        model = Car
        fields = '__all__' # Qual campo da tabela Car você quer?



# Forma errada usando o modo Form simples

""" class CarForm(forms.Form): #forms.Form já é um formulário pronto do django.
    model = forms.CharField(max_length= 200)
    brand = forms.ModelChoiceField(Brand.objects.all()) #Puxando as marcas pelo query sets.
    factory_year = forms.IntegerField() 
    model_year = forms.IntegerField() #ano
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField() # Repete os mesmos campos do modelo.

    def save(self):
        car = Car(
            model = self.cleaned_data['model'], 
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car """