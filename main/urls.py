from django.urls import path
from .views import index, order_form, get_category_portfolio, logout_our, register

urlpatterns = [
    path('', index, name='home'),
    path('order_form', order_form, name='order_form'),
    path('get-category-izdeliya/<int:category_id>', get_category_portfolio, name='get_category_izdeliya'),
    path('logout/', logout_our, name='logout' ),
    path('register/', register, name='register' )
]
