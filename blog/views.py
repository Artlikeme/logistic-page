from django.shortcuts import render,redirect
from .models import Articles
from main.models import Form
from main.forms import FunForm

from django.views.generic import DetailView


def blog(request):

    form = FunForm()

    articles = Articles.objects.order_by('-date')

    return render(request,'blog/blog.html', {'articles':articles,'form': form})


class ArticleDetailview(DetailView):
    model = Articles
    template_name = 'blog/detail_view.html'
    context_object_name = 'article'