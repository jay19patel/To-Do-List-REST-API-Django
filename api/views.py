from django.shortcuts import render
from api.serializers import TaskSerializer
from api.models import Task

from rest_framework.decorators import api_view
from rest_framework.response  import Response

# all task get
@api_view(['GET'])
def myapi(request):
    task= Task.objects.all()
    serializer =TaskSerializer(task,many=True)
    return Response({'Status':200,'Paylod':serializer.data,'Message':'All Task Is Here'})


# get id task
@api_view(['GET'])
def taskget(request,id):
    task= Task.objects.get(id=id)
    serializer =TaskSerializer(instance=task)
    return Response({'Status':200,'Paylod':serializer.data,'Message':'All Task Is Here'})
    
# post new task
@api_view(['POST'])
def taskadd(request):
    data= request.data
    serializer =TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Status':200,'Paylod':serializer.data,'Message':'Added New Task'})
    else:
        return Response({'Status':403,'Paylod':'Error ','Message':'Somthing Wrong'})
    
# update task
@api_view(['POST'])
def taskupdate(request,id):
    task= Task.objects.get(id=id)
    data= request.data
    serializer =TaskSerializer(instance=task ,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Status':200,'Paylod':serializer.data,'Message':'Update Task'})
    else:
        return Response({'Status':403,'Paylod':'Error ','Message':'Somthing Wrong'})



# delete task
@api_view(['DELETE'])
def taskdelete(request,id):
    task= Task.objects.get(id=id)
    task.delete()
    return Response({'Status':200,'Paylod':'data deleted','Message':'Deleted Task'})



