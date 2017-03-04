from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task,Project
from .serializer import TaskSerializer, ProjectSerializer
from django.http import Http404


from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

####################################################
#      Codepasta from internets; skroll down
####################################################

# Lists all Tasks or create a new one
# tasks/
class TaskList(APIView):
    def get(self, request): 
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
        '''
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''
        
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    def put(self, request):
        username = request.data.get('username', '')
        old_password = request.data.get('old_password', '')
        new_password = request.data.get('new_password', '')
        user = authenticate(username=username, password=old_password)
        if not user:
            return Response({'status': 'fail'})
        user.set_password(new_password)
        return Response({'status': 'ok'})

    def delete(self, request): 
        title = request.query_params.get('username', '')
        Task.objects.get(title=username).delete()
        return Response({'status': 'ok'})
     '''   

class TaskDetail(APIView):

    def get_object(self, pk):
        try: 
            return Task.objects.get(pk=pk)
        except Task is not None.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        task = TaskSerializer(task)
        return Response(task.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


####################################################
#       (Seems like) working part of code
####################################################
# TODO: 
# Fall apart every time when I want to get wrong url address
# Add logs

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def task_list(request):
    """
    List all code task, or create a new task.
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JSONResponse(serializer.data)
       # return Response(serializer.data) # Why doesn't work? I NEED TO KNOW

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    """
    Retrieve, update or delete a task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=204)

@csrf_exempt
def project_list(request):
    """
    List all code task, or create a new project.
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JSONResponse(serializer.data)
       # return Response(serializer.data) # Why doesn't work? I NEED TO KNOW

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def project_detail(request, pk):
    """
    Retrieve, update or delete a project.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=204)