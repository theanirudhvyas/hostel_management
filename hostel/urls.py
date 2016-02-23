from django.conf.urls import url
from . import views

app_name = 'hostel'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^student_details',views.student_details, name='student_details')
    #url(r'^logout/$', 'django.contrib.auth.views.logout'),
]
