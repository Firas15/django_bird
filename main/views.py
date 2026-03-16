from django.shortcuts import render, redirect
from .models import Portfolio,Category
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


def index(request):
    categories = Category.objects.all().order_by('-order')
    return render(request, 'index.html', {"categories":categories})


def order_form(request):
    return render(request, 'order-form.html')

def logout_our(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,"register.html",{'form':form})



def get_category_portfolio(request, category_id):
    category = Category.objects.get(id = category_id)
    izdelie = Portfolio.objects.filter(category = category)
    #json
    spisok = []
    for i in izdelie:
        spisok.append({
            "id":i.id,
            "title":i.title,
            "img":i.img.url,
            "description":i.description,
            "dead_line":i.dead_line
        })
    return JsonResponse({
        "izdeliya":spisok,
        "category_name":category.name
    })