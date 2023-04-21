from django import forms
from cars.models import Brand, Car

# Forma correta usando o ModelForm

class CarModelForm(forms.ModelForm): # Isso substitui tudo isso comentado de cima, pq liga diretamente com o model Car
    class Meta:
        model = Car
        fields = '__all__' # Qual campo da tabela Car você quer?

# Validações (quando o is_valid da view for acionado ele vai verificar se tudo aqui está válido)

    def clean_value(self): # clean diz que essa é uma função de validação e o nome do campo validado
        value = self.cleaned_data.get('value') # Capturando o valor de value
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$ 20.000,00')
        else:
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975') # Aqui o factory_year é o campo e não a variável
        else:
            return factory_year



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