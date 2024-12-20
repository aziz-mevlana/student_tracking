from django.shortcuts import render
from news.models import News,Category



def index(request):
    context = {
        "news": News.objects.filter(is_active=True, is_home=True),
        "category": Category.objects.all()
    }
    return render(request, "news/index.html", context)

def news(request):
    context = {
        "news": News.objects.filter(is_active=True),
        "category": Category.objects.all()
    }
    return render(request, "news/news.html", context)

def news_details(request, slug):
    slug = News.objects.get(slug=slug)
    return render(request, "news/news-details.html", {
        "new": slug
    })
    
def deneme(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "news/deneme.html", context)



