from django.contrib import admin
from .models import Portfolio, Category, Order


admin.site.register(Category)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("category","title","dead_line")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","phone","data","get_id")

    def get_id(self,obj):
        return obj.id
    get_id.short_description = "Номер заказа"
