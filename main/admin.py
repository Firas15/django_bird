from django.contrib import admin
from .models import Portfolio, Category


admin.site.register(Category)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("category","title","dead_line")