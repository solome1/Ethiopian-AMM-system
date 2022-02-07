from itertools import count
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import MyProducts, CustomProductsItem
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .models import TodoListItem, CustomProductsItem
from .forms import TodoListForm, CustomProductsForm, CreateForm
#from django.http import HttpResponse

# Create your views here.
def index(request):
    dests = MyProducts.objects.all()
    return render(request, 'index.html', {'dests': dests})

def showproducts(request):
    avail_products = MyProducts.objects.all()
    return render(request, 'products.html', {'avail_products': avail_products})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    user = request.user
    # change database, add user for each user in database
    user_product = MyProducts.objects.filter(user_id = user.id)
    return render(request, "dashboard.html", {"userpro": user_product})

def productForm(request):
    return render(request, "product_form.html")


def saveProduct(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.user = request.user
            form.save()
            messages.info(request, "Product Created SuccessFullly !")
            return redirect('/dashboard/productForm/')
            #return HttpResponseRedirect('/')
        else:
            messages.info(request, "Invalid From")
            #return HttpResponse('Form not valid')
    else:
        form = TodoListForm()
    return render(request, 'product_form.html')
'''
def saveProduct(request):
    if request.method == "POST":
        form = CustomProductsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Product Created SuccessFullly !")
            return redirect('/dashboard/productForm/')
            #return HttpResponseRedirect('/')
        else:
            messages.info(request, "SomeThing Went Wrong")
            #return HttpResponse('Form not valid')
    else:
        form = TodoListForm()
    return render(request, 'product_form.html')
'''    



def home(request):
    context = {
        'items': TodoListItem.objects.all()
    }
    return render(request, 'home.html', context)

def enter_task(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Form not valid')
    else:
        form = TodoListForm()
    return render(request, 'form.html', {'form': form})

