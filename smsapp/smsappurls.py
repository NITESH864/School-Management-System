from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('about2/',views.about2,name='about2'),
    path('about3/',views.about3,name='about3'),
    path('about4/',views.about4,name='about4'),
    path('about5/',views.about5,name='about5'),
    path('about6/',views.about6,name='about6'),
    path('about7/',views.about7,name='about7'),
    path('about8/',views.about8,name='about8'),
    path('login/',views.login,name='login'),
    path('acadmic/',views.acadmic,name='acadmic'),
    path('carrier/',views.carrier,name='carrier'),
    path('transport/',views.transport,name='transport'),
    path('medical/',views.medical,name='medical'),
    path('smartclass/',views.smartclass,name='smartclass'),
    path('otfacilities/',views.otfacilities,name='otfacilities'),  
    path('admission1/',views.admission1,name='admission1'),
    path('admission2/',views.admission2,name='admission2'),
    path('admission3/',views.admission3,name='admission3'),
    path('media1/',views.media1,name='media1'),
    path('media2/',views.media2,name='media2'),

    path('logcode/',views.logcode,name='logcode'),



]