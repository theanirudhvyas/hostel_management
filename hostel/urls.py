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
    url(r'^show_requests/$', views.show_requests, name='show_requests'),
    url(r'^show_change/(?P<id>\d+)/$', views.show_change, name='show_change'),
    url(r'^show_swap/(?P<id>\d+)/$', views.show_swap, name='show_swap'),
    url(r'^logout/$', views.logout1, name='logout'),
    url(r'^read_csv/$', views.read_csv, name='read_csv'),
    url(r'^deallocate/$', views.deallocate, name='deallocate'),
    url(r'^create_room/$', views.create_room, name='create_room'),
    url(r'^show_vacancy/$', views.show_vacant, name='show_vacancy'),
    url(r'^show_students/$', views.show_students, name='show_students'),
    url(r'^success/$', views.success, name='success')
    #url(r'^logout/$', 'django.contrib.auth.views.logout'),
]

handler404  = 'views.handler404'

