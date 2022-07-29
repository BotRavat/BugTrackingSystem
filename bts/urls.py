 

from django.contrib import admin
from django.urls import path,include
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.btshome,name='home'),
    path('bts',views.btshome,name='home'),
    path('bugreport',views.bugreport,name='bugreport'),
    path('addbug',views.addbug,name='addbug'),
    path('delete/<int:sno> ',views.deletebug,name='deletebug'),
    path('bugdetail/<int:sno>',views.bugdetail,name='bugdetail'),
    path('updatebug/<int:sno>',views.updatebug,name='updatebug'),
    path('projectreport',views.projectreport,name='projectreport'),
    path('projectreportdata/<str:projectname>',views.projectreportdata,name='projectreportdata'),
    path('addusers',views.addusers,name='addusers'),
   
   
   
]

 