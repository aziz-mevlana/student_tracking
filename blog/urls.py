from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns  = [
    path('post',views.post, name="post"),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:id>/edit/',views.post_edit,name='post_edit'),
    path('post/<int:id>/delete/',views.post_delete ,name ='post_delete'),
] 
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
