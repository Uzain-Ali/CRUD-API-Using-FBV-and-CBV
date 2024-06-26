from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentData
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class StudentList(ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class= StudentSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    filterset_fields = ['name','city']
