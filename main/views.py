from django.shortcuts import render,redirect
from .models import Form
from .forms import FunForm
from blog.models import Articles

# Create your views here.
def index(request):
    # сохраненни в бд
    error = ''
    if request.method == 'POST':
        form = FunForm(request.POST)
        # если корректно то сохраняем и перенаправялем на главную
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Try again'

    # работа с статьями из блога(вывод двух последних статей из бд)
    article = Articles.objects.order_by('-date')[:2]

    # работа с формой ,подключение формы к шаблону
    form = FunForm()
    data = {'form': form,'error':error, 'article':article}

    return render(request,'main/index.html', data)



def privacy(request):
    return render(request, 'main/privacy.html')


def terms(request):
    return render(request, 'main/terms.html')