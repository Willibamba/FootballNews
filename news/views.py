from django.shortcuts import render, redirect
from reporter.models import Article
from django.template.defaultfilters import dictsortreversed


# Create your views here.

def news(request):
    # QuerySet to get all articles and reverse it through primary key 
    articles = Article.objects.all()
    articles = dictsortreversed(articles, "pk")
    return render(request, "news/index.html", {"articles": articles})

def news_view(request, id):
    # QuerySet to get the specific article by the id 
    article = Article.objects.get(id=id)
    return render(request, "news/view.html", {'article': article})

def female(request):
    # QuerySet to get the articles with Female category and reverse it through primary key
    articles = Article.objects.filter(article_category="Female")
    articles = dictsortreversed(articles, "pk")
    return render(request, "news/index.html", {"articles": articles})

def male(request):
    # QuerySet to get the articles with Male category and reverse it through primary key
    articles = Article.objects.filter(article_category="Male")
    articles = dictsortreversed(articles, "pk")
    return render(request, "news/index.html", {"articles": articles})

def world_cup(request):
    # QuerySet to get the arcticles with World Cp category and reverse it through primary
    articles = Article.objects.filter(article_category="World Cup")
    articles = dictsortreversed(articles, "pk")
    return render(request, "news/index.html", {"articles": articles})