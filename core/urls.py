from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^task/get-all/$', views.get_all_tasks),
    url(r'^task/get-by-dk/(?P<pk>[0-9]+)/$', views.get_task_by_dk),
    url(r'^task/edit/(?P<pk>[0-9]+)/$', views.edit_task),
    url(r'^task/delete/(?P<pk>[0-9]+)/$', views.delete_task),
    url(r'^task/add/$', views.add_task),

    url(r'^users/register', 'views.create_auth'),

   # url(r'^users/$', views.UserList.as_view()),
   # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
 

    url(r'^project/get-all/$', views.get_all_projects),
    url(r'^project/get-by-dk/$', views.get_project_by_dk),
    url(r'^project/edit/$', views.edit_project),
    url(r'^project/delete/$', views.delete_project),
    url(r'^project/add/$', views.add_project),
    
]
'''
     url(r'^tasks/', views.TaskList.as_view()),
     url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
     url(r'^tasks/$', views.task_list),
     url(r'^tasks/(?P<pk>[0-9]+)/$', views.task_detail),
     url(r'^projects/$', views.project_list),
     url(r'^projects/(?P<pk>[0-9]+)/$', views.project_detail),
'''
     
'''
    url(r'^task/get-corresponding-project/$', views.get_projects_of_task),
     url(r'^project/get-corresponding-tasks$', views.get_tasks_of_project),
     
     

     
'''




