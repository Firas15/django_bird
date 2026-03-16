from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="Вид работы")
    img = models.ImageField(upload_to="category_img1", verbose_name="Фотография", default=None, blank= True)
    description = models.TextField(verbose_name='Описание', default=None,blank= True)
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
