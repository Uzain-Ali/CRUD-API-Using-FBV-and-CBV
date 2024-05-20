from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


class StudentROMVS(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer