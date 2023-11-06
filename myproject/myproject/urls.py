"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from myapp.views import*
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/',include('myapp.urls')),
    # path('',views.home,name="h"),
     path('',views.index,name="h"),





    path('adddep/',views.adddep,name="adddep"), 
 #  path('depview/',views.depview,name="depview"),


    path('sturegi/',views.StuRegi,name="studregi"),
    path('viewstud/',views.viewstud,name="viewstud"),
    path('studapprove/<int:id>/',views.studapprove),
    path('reject/<int:id>/',views.reject),
    path('viewapprovest/',views.viewapprovest,name="viewapprovest"),
  

    path('editstudent/',views.editstudent,name="editstudent"),
    # path('updatestudview/',views.updatestudview,name="updatestudview"),



    path('teachregi/',views.TeachRegi,name="teacherregi"),
    path('teacherview/',views.teacherview,name="teacherview"),
    #  path('updateteacherview/',views.updateteacherview,name="updateteacherview"),
     path('editteacher/',views.editteacher,name="editteacher"),

    path('logins/',views.logins,name="logins"),
    path('lgout/',views.lgout,name='lgout'),



    path('adminhome/',views.adminhome,name="adminhome"),
    path('adminhome1/',views.adminhome1,name="adminhome1"),

    path('teacherhome/',views.teacherhome,name="teacherhome"),
    path('studhome/',views.studhome,name="studhome"),
    path('index/',views.index,name="index"),
    path('regi/',views.regi,name="regi"),
    path('table/',views.table,name="table"),
    path('viewdpbyst/',views.viewdpbyst,name="viewdpbyst"),
    path('viewdpbyte/',views.viewdpbyte,name="viewdpbyte"),

    ]
