from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Task,Project
from .serializer import TaskSerializer,ProjectSerializer,UserSerializer
from django.http import Http404
from rest_framework.decorators import api_view

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from django.contrib.auth.models import User

####################################################
#       Working (no) part of code
####################################################

# Fall apart every time when I want to get wrong url address

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



####################################################################

@api_view(['GET'])
def get_all_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JSONResponse(serializer.data)
    # return Response(serializer.data) # Why it doesn't work? I NEED TO KNOW

@api_view(['GET'])
def get_task_by_dk(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    serializer = TaskSerializer(task)
    return JSONResponse(serializer.data)

@api_view(['PUT'])
def edit_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
        
    data = JSONParser().parse(request)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data)
        
    return JSONResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
        
    task.delete()
    return HttpResponse(status=204)

@api_view(['POST'])
def add_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

# @api_view(['GET'])
# def get_project_of_task(request):
   # project = Task.objects.get()
   # serializer = TaskSerializer(tasks, many=True)
   # return JSONResponse(serializer.data)

####Project

@api_view(['GET'])
def get_all_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JSONResponse(serializer.data)
    # return Response(serializer.data) # Why it doesn't work? I NEED TO KNOW

@api_view(['GET'])
def get_project_by_dk(request, pk):
    try:
        project = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    serializer = TaskSerializer(project)
    return JSONResponse(serializer.data)

@api_view(['PUT'])
def edit_project(request, pk):
    try:
        project = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
        
    data = JSONParser().parse(request)
    serializer = TaskSerializer(project, data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data)
        
    return JSONResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_project(request, pk):
    try:
        project = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)
        
    project.delete()
    return HttpResponse(status=204)

@api_view(['POST'])
def add_project(request):
    data = JSONParser().parse(request)
    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)



