from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentData
from rest_framework.generics import ListAPIView
# Create your views here.


class StudentList(ListAPIView):
    queryset = StudentData.objects.filter(passby="uzain95")
    serializer_class= StudentSerializer