from django.conf.urls import url
from basicapp import views

#template tagging
app_name ='basicapp' #global name=app_name
urlpatterns =[
   url(r'^relative/$' , views.relative , name='relative'),
   url(r'^other/$' , views.other , name='other'),
   ]
