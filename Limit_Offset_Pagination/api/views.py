from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentData
from rest_framework.generics import ListAPIView
from .mypagination import MyLimitOffsetPagination


# Create your views here.
class StudentList(ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination