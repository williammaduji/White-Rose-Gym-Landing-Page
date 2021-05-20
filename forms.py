from django.forms import ModelForm
from .models import Forms


class Form(ModelForm):
    class Meta:
        model = Forms
        fields = '__all__'
