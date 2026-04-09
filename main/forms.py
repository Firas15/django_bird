from django import forms
from .models import Order

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["theme","name","email","phone","tg_nick","descp_order"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        #if self.user and self.user.is_authenticated:
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user and self.user.is_authenticated:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


