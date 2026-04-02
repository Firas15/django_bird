from django import forms
from .models import Order

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["theme","name","email","phone","tg_nick","descp_order"]
