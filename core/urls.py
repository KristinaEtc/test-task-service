from django.conf.urls import url
from core import views

urlpatterns = [
    # url(r'^tasks/', views.TaskList.as_view()),
    # url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
     url(r'^tasks/$', views.task_list),
     url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail),
]



