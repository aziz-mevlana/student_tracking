from django.shortcuts import render
from news.models import News,Category
from django.contrib.auth.models import User
from account.models import Profile
from graduates.models import GraduatingStudents
from student_projects.models import StudentSubmission


def index(request):
    # Aktif öğrenci sayısını hesaplama
    active_students_count = Profile.objects.filter(is_verified=True).count()
    
    # Mezun sayısını hesaplama
    graduates_count = GraduatingStudents.objects.count()
    
    # Onaylanmış projelerin sayısını hesaplama
    approved_projects_count = StudentSubmission.objects.filter(is_approved=1).count()
    
    context = {
        "news": News.objects.filter(is_active=True, is_home=True),
        "category": Category.objects.all(),
        "active_students_count": active_students_count,
        "graduates_count": graduates_count,
        "approved_projects_count": approved_projects_count
    }
    return render(request, "news/index.html", context)

def news(request):
    context = {
        "news": News.objects.filter(is_active=True),
        "category": Category.objects.all()
    }
    return render(request, "news/news.html", context)

def news_details(request, slug):
    news_item = News.objects.get(slug=slug)
    
    # Mevcut haber dışındaki aktif haberlerden en son 3 tanesini al
    related_news = News.objects.filter(
        is_active=True
    ).exclude(
        id=news_item.id
    ).order_by('-published_date')[:3]
    
    return render(request, "news/news-details.html", {
        "new": news_item,
        "related_news": related_news
    })
    
def deneme(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "news/deneme.html", context)



