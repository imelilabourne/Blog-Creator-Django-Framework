from django import forms
from base.models import ProductPic, TravelPic, FoodPic

class ProductPicForm(forms.ModelForm):
    class Meta:
        model = ProductPic
        fields = ('image', 'location', 'title', 'story', 'price')

class TravelPicForm(forms.ModelForm):
    class Meta:
        model = TravelPic
        fields = ('image', 'location', 'title', 'story', 'TravelExpenses')

class FoodPicForm(forms.ModelForm):
    class Meta:
        model = FoodPic
        fields = ('image', 'location', 'title', 'story', 'price')

    