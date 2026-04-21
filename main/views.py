from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Portfolio, Category, Order
from django.http import JsonResponse
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import Order_form
from django.core.mail import send_mail


def index(request):
    send_mail("Тестовое письмо","Пришел заказ",None,["vishivka2026@yandex.ru"],fail_silently=False)
    categories = Category.objects.all().order_by('-order')
    return render(request, 'index.html', {"categories": categories})


def order_form(request):
    if request.method == "POST":
        form = Order_form(
            request.POST,
            user=request.user if request.user.is_authenticated else None
        )
        if form.is_valid():
            order = form.save()
            return redirect(f"/accept_order/{order.id}")
    else:
        form = Order_form()

        return render(request, 'order-form.html', {'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request,'profile.html',{"orders":orders})


def about(request):
    return render(request, 'about.html')


def login_our(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
        messages.error(request, 'Неверный логин или пароль.')
        return redirect('login')
    return render(request, 'login.html', {'form': AuthenticationForm()})

def accept_order(request, number):
    return render(request,"accept_order.html",{'number':number})




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
            "img_finish":  i.img_finish.url,
            "description": i.description,
            "dead_line":   i.dead_line,
        })

    return JsonResponse({
        "izdeliya":      spisok,
        "category_name": category.name,
    })