from django.conf.urls import url
from . import views

app_name = 'hostel'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^student_details',views.student_details, name='student_details'),
    url(r'^allocate/$', views.allocate, name='allocate'),
    url(r'^swap/$', views.swap, name='swap'),
    url(r'^change/$', views.change, name='change'),
    url(r'^change_req/$', views.change_request, name='change_req'),
    url(r'^swap_req/$', views.swap_request, name='swap_req'),
    url(r'^swap/$', views.swap, name='swap'),
    url(r'^swap_ack/$', views.swap_ack, name='swap_ack'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout'),
]
