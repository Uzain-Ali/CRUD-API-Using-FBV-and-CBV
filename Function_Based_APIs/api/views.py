from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.
# By default GET
# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello World'})

# GET mentioned
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'Hello Wor ld'})

# POST Method
# @api_view(['POST','GET'])
# def hello_world(request):
#     if request.method =="GET":
#         return Response({'msg': 'This is GET Request'})
#     if request.method =="POST":
#         print(request.data)
#         return Response({'msg':'This is POST Request', 'data':request.data})



# CRUD using api_view
@api_view(['GET', 'POST', 'PUT','PATCH', 'DELETE'])
def student_api(request, pk = None):
    if request.method =='GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu =Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method =="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        # id = request.data.get('id')
        id = pk

        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == "PATCH":
        # id = request.data.get('id')
        id = pk

        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    if request.method == "DELETE":
        # id =request.data.get('id')
        id = pk

        stu = Student.objects.get(pk = id)
        stu.delete()
        return Response({'msg':'Data Deleted...'})