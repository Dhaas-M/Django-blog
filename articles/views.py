from hmac import new
from django.http import HttpResponse
from django.shortcuts import redirect, render
from flask import url_for
from platformdirs import user_log_path
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/articles.html', {'articles': articles})


def article_details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'article/article_detail.html', {'article': article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()    

    return render(request, 'article/article_create.html',{'form':form})    



def populate(request):
    l=['hello', 'new', 'ok']
    for i in l:
        article = Article()    
        article.title = i
        article.save()

    return HttpResponse('ok')    
