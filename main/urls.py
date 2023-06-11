from django.urls import path
from . import views
urlpatterns =[
    path("",views.home,name='home'),
    path("blog/",views.blog,name='blog'),
    path("blog/details",views.blog_details,name='blog_details'),
    path("business/",views.business,name='business'),
    path("licencing/",views.licencing,name='licencing'),
    path("taxation/",views.taxation,name='taxation'),
    path("ipr/",views.ipr,name='ipr'),
    path("it/",views.it,name='it'),
    path('business/<slug:slug>/', views.business_registration, name='business_registration'),
    path('licencing/<slug:slug>/', views.registration_licencing, name='registration_licencing'),
    path('taxation/<slug:slug>/', views.gst_incometax, name='gst_incometax'),  
    path('ipr/<slug:slug>/', views.intellectual_property, name='intellectual_property'), 
    path('it/<slug:slug>/', views.information_technology, name='information_technology'), 
    path('other/<slug:slug>/', views.other_service, name='other_service'), 
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)