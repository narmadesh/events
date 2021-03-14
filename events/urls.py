from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.events, name='create'),
    path('like/', views.like, name='like'),
    path('unlike/', views.unlike, name='unlike'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 