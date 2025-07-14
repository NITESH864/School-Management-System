from django.urls import path
from.import views
urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminbase/',views.adminbase,name='adminbase'),
    path('viewenquiries/',views.viewenquiries,name='viewenquiries'),
    path('delenq/<id>',views.delenq,name='delenq'),
    path('addclass/',views.addclass,name='addclass'),
    path('viewclass/',views.viewclass,name='viewclass'),
    path('delcla/<id>',views.delcla,name='delcla'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('addsubject/',views.addsubject,name='addsubject'),
    path('viewsubject/',views.viewsubject,name='viewsubject'),
    path('editsubject/<id>',views.editsubject,name='editsubject'),

    path('delsub/<id>',views.delsub,name='delsub'),
    path('editclass/<id>',views.editclass,name='editclass'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('viewteacher/',views.viewteacher,name='viewteacher'),
    path('editteacher/<id>',views.editteacher,name='editteacher'),

    path('delteach/<id>',views.delteach,name='delteach'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('delst/<id>',views.delst,name='delst'),
    path('editstudent/<id>',views.editstudent,name='editstudent'),
    path('addnoti/',views.addnoti,name='addnoti'),
    path('viewnoti/',views.viewnoti,name='viewnoti'),



    
]