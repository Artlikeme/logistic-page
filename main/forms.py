from .models import Form
from django.forms import ModelForm,TextInput

class FunForm(ModelForm):
# обязательный класс для полей сз формы из модулей
    class Meta:
        model = Form
        fields = ['name','phone','email']
# создание вилда для формы джанго
        widgets = {
            'name': TextInput(attrs={
                'class':'input input--user',
                'placeholder':"Your name"
            }),
            'phone': TextInput(attrs={
                'class':'input input--phone',
                'placeholder':"Your Phone"
            }),
            'email': TextInput(attrs={
                'class':'input input--email',
                'placeholder':"Your Email"
            }),

        }