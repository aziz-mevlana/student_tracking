from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from graduates.models import GraduatingStudents, Category


def graduates(request):
    graduate_slug = request.GET.get('graduate')
    graduate_detail = None
    
    if graduate_slug:
        graduate_detail = get_object_or_404(GraduatingStudents, slug=graduate_slug)
    
    context = {
        "graduates": GraduatingStudents.objects.all(),
        "categories": Category.objects.all(),
        "graduate_detail": graduate_detail
    }
    return render(request, "graduates/graduatingstudents.html", context)

def graduates_by_category(request, slug):
    graduate_slug = request.GET.get('graduate')
    graduate_detail = None
    
    if graduate_slug:
        graduate_detail = get_object_or_404(GraduatingStudents, slug=graduate_slug)
        
    context = {
        "graduates": GraduatingStudents.objects.filter(category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug,
        "graduate_detail": graduate_detail
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
            'img_url': graduate.img.url
        }
        return JsonResponse({'success': True, 'graduate': data})
    
    # AJAX isteği değilse doğrudan mezunlar sayfasına yönlendir
    return graduates_by_category(request, graduate.category.slug)