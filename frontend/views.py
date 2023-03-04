from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django .http import JsonResponse


@csrf_exempt
def HomePage(request):
    return render(request,'Home.html')


# def Deleteapi(request):
#     json_data = json.loads(request.body)
#     print(json_data)
#     response_data = {"message":"recive data succesfully"}     
#     return JsonResponse(response_data)