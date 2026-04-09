from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Вид работы", max_length=100)
    img = models.ImageField(upload_to="category_img1", verbose_name="Фотография", blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default= 0)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    category = models.ForeignKey(Category, verbose_name= "Вид работы", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name= "Название изделия")
    img = models.ImageField(upload_to="portfolio_img1", verbose_name="Фотография")
    img_finish = models.ImageField(upload_to="portfolio_img_finish1", verbose_name="Фотография готового изделия")
    description = models.TextField(verbose_name='Описание')
    dead_line = models.IntegerField(verbose_name="Сроки изготовления в днях")




    def __str__(self):
        return self.title
class Order(models.Model):
    choice = [
        ('photo','Вышивка по фото'),
        ('personal', 'Персональный дизайн вышивки'),
        ('restoration', 'Восстановление одежды'),
        ('consultation', 'Консультация'),
        ('other', 'Другое'),
    ]
    theme = models.CharField(max_length=200,choices=choice,verbose_name="Тема заказа")
    name =models.CharField(max_length=200,verbose_name="Имя клиента")
    email =models.EmailField(max_length=100,verbose_name="Email")
    phone =models.CharField(max_length=50,verbose_name="Номер телефона")
    tg_nick =models.CharField(max_length=200,verbose_name="Телеграмм")
    descp_order =models.TextField(verbose_name="Описание заказа")
    data =models.DateTimeField(auto_now_add= True, verbose_name="Дата заказа")
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)




    def __str__(self):
        return f"Заказ № {self.id}"