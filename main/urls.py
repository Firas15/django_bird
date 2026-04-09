from django.urls import path
from .views import index, order_form, get_category_portfolio, logout_our, register, login_our, about, accept_order, profile

urlpatterns = [
    path('', index, name='home'),
    path('order_form', order_form, name='order_form'),
    path('about/', about, name='about'),
    path('get-category-izdeliya/<int:category_id>', get_category_portfolio, name='get_category_izdeliya'),
    path('logout/', logout_our, name='logout'),
    path('register/', register, name='register'),
    path('login-post/', login_our, name='login_post'),
    path('accept_order/<str:number>', accept_order, name='accept_order'),
    path('profile/', profile, name='profile'),
]