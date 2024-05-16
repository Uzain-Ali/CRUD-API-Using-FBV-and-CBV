from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt, name = 'dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body #JSON data come from request
        stream = io.BytesIO(json_data) #Binary form of data in memory
        python_data = JSONParser().parse(stream) #stream got converted into python_native_data_type
        id = python_data.get('id', None) #fetch id from python data
        if id is not None: #check id != none, means id exists
            stu = Student.objects.get(id=id) #matching the id with the objects in the model
            serializer = StudentSerializer(stu) #Python data convert into complex data
            json_data = JSONRenderer().render(serializer.data)   #rendering data from complex data    
            return HttpResponse(json_data, content_type = 'application/json') #Sending Response to Request
        stu = Student.objects.all() #if id not exist it'll send complete data
        serializer = StudentSerializer(stu, many=True) #converting complete data into complex form
        json_data = JSONRenderer().render(serializer.data)   #rendering data from complex data     
        return HttpResponse(json_data, content_type = 'application/json') #Sending Response to Request


    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream =io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json') 

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream =io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data = python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')


    def delete(self, request, *args, **kwargs):
            json_data = request.body
            stream =io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg':'Data Deleted!!'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, content_type = 'application/json')
            return JsonResponse(res, safe=False)






