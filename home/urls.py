from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('uthiru-ruthimitu/projects/', views.projects, name='projects'),
    path('uthiru-ruthimitu/events/', views.events, name='events'),
    path('uthiru-ruthimitu/ward-facilities/', views.facilities, name='facilities'),
    path('uthiru-ruthimitu/uthiru-ruthimitu/', views.uthimitu, name='uthimitu'),
    path('uthiru-ruthimitu/our-history/', views.history, name='history'),
    path('uthiru-ruthimitu/committee/', views.committee, name='committee'),
    path('uthiru-ruthimitu/emergency-contacts/', views.emergency, name='emergencies'),
    path('uthiru-ruthimitu/contact-us/', views.contacts, name='contacts'),
    path('uthiru-ruthimitu/garbage-pickup/', views.garbage, name='garbage'),
    path('uthiru-ruthimitu/ward-programmes/', views.programmes, name='programmes'),
    path('uthiru-ruthimitu/blogs/', views.blogs, name='blogs'),    
    path('uthiru-ruthimitu/map/', views.maps, name='maps'),
    path('uthiru-ruthimitu/downloads/', views.downloads, name='downloads'),
    path('uthiru-ruthimitu/tenders/', views.tenders, name='tenders'),  
    path('uthiru-ruthimitu/gallery/', views.gallery, name='gallery'),

    # Forms URLS Patterns
    path('uthiru-ruthimitu/birth_certificate_registration/', views.birth, name='birth'),
    path('uthiru-ruthimitu/<slug:slug>/', views.article_detail, name='article-detail'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)