from .models import TodoListItem, CustomProductsItem, MyProducts
from django.forms import ModelForm

class TodoListForm(ModelForm):
    class Meta:
        model = TodoListItem
        fields = ['content']

class CustomProductsForm(ModelForm):
    class Meta:
        model = CustomProductsItem
        fields = ['name', 'desc', 'price', 'seller']

class CreateForm(ModelForm):
    class Meta:
        model = MyProducts
        fields = ['name','desc', 'price', 'user', 'img']