from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.schedule_list, name='schedule_list'),
    url(r'^insert/$',views.enroll_post, name='enroll_insert'),
    url(r'^memo/$',views.enroll_memo, name='enroll_memo'),
]
