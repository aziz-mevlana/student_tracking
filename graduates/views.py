from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from graduates.models import GraduatingStudents, Category
from django.template.defaulttags import register


# Template filter for accessing dictionary with a variable key
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def graduates(request):
    graduate_slug = request.GET.get('graduate')
    graduate_detail = None
    
    if graduate_slug:
        graduate_detail = get_object_or_404(GraduatingStudents, slug=graduate_slug)
    
    # Kategorilere göre mezun sayısını hesapla
    categories = Category.objects.all()
    graduate_counts = {}
    
    # Her kategori için mezun sayısını hesapla
    for category in categories:
        count = GraduatingStudents.objects.filter(category=category).count()
        graduate_counts[category.slug] = count
    
    # Toplam mezun sayısı
    graduate_counts['total'] = GraduatingStudents.objects.count()
    
    context = {
        "graduates": GraduatingStudents.objects.all(),
        "categories": categories,
        "graduate_detail": graduate_detail,
        "graduate_counts": graduate_counts
    }
    return render(request, "graduates/graduatingstudents.html", context)

def graduates_by_category(request, slug):
    graduate_slug = request.GET.get('graduate')
    graduate_detail = None
    
    if graduate_slug:
        graduate_detail = get_object_or_404(GraduatingStudents, slug=graduate_slug)
        
    # Kategorilere göre mezun sayısını hesapla
    categories = Category.objects.all()
    graduate_counts = {}
    
    # Her kategori için mezun sayısını hesapla
    for category in categories:
        count = GraduatingStudents.objects.filter(category=category).count()
        graduate_counts[category.slug] = count
    
    # Toplam mezun sayısı
    graduate_counts['total'] = GraduatingStudents.objects.count()
        
    context = {
        "graduates": GraduatingStudents.objects.filter(category__slug=slug),
        "categories": categories,
        "selected_category": slug,
        "graduate_detail": graduate_detail,
        "graduate_counts": graduate_counts
    }
    return render(request, "graduates/graduatingstudents.html", context)

def get_graduate_detail(request, slug):
    """AJAX isteği ile mezun detaylarını getiren API"""
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        graduate = get_object_or_404(GraduatingStudents, slug=slug)
        data = {
            'name': graduate.name,
            'surname': graduate.surname,
            'description': graduate.description,
            'email': graduate.email,
            'graduation_date': graduate.graduation_date.strftime('%d.%m.%Y'),
            'category': graduate.category.name,
            'img_url': graduate.img.url,
            'linkedin': graduate.linkedin,
            'github': graduate.github,
            'twitter': graduate.twitter,
            'instagram': graduate.instagram,
            'website': graduate.website,
            'cv_file_url': graduate.cv_file.url if graduate.cv_file else None
        }
        return JsonResponse({'success': True, 'graduate': data})
    
    # AJAX isteği değilse doğrudan mezunlar sayfasına yönlendir
    return graduates_by_category(request, graduate.category.slug)