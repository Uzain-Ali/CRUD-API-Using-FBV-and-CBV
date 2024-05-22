from django.shortcuts import render
from .serializers import StudentSerializer
from .models import StudentData
from rest_framework.generics import ListAPIView
# Create your views here.


class StudentList(ListAPIView):
    queryset = StudentData.objects.all()
    serializer_class= StudentSerializer

    def get_queryset(self):
        user = self.request.user
        return StudentData.objects.filter(passby=user)