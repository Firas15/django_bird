from django.shortcuts import render, redirect
from .models import Portfolio, Category
from django.http import JsonResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    categories = Category.objects.all().order_by('-order')
    return render(request, 'index.html', {"categories": categories})


def order_form(request):
    return render(request, 'order-form.html')

def login_our(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
        messages.error(request, 'Неверный логин или пароль.')
        return redirect('home')
    return render(request, 'login.html', {'form': AuthenticationForm()})

def logout_our(request):
    messages.success(request, 'Вы вышли из аккаунта.')
    logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
        return render(request, "register.html", {'form': form})
    form = UserCreationForm()
    return render(request, "register.html", {'form': form})


def get_category_portfolio(request, category_id):
    category = Category.objects.get(id=category_id)
    izdelie = Portfolio.objects.filter(category=category)

    spisok = []
    for i in izdelie:
        spisok.append({
            "id":          i.id,
            "title":       i.title,
            "img":         i.img.url,
            "description": i.description,
            "dead_line":   i.dead_line,
        })

    return JsonResponse({
        "izdeliya":      spisok,
        "category_name": category.name,
    })