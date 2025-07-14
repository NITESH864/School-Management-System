from django.urls import path
from.import views


urlpatterns=[
    path('studentapp',views.studenthome,name='studenthome'),
    path('stuattend',views.stuattend,name='stuattend'),
    path('studentlogout',views.studentlogout,name='studentlogout'),
    path('stchangepass',views.stchangepass,name='stchangepass'),
    path('stuslm',views.stuslm,name='stuslm'),
    path('stprofile',views.stprofile,name='stprofile'),
    path('uploadpic',views.uploadpic,name='uploadpic'),
    
]