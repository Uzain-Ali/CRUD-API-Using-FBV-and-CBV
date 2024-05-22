from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    passby = models.CharField(max_length=50)


    class Meta:
        db_table = "student_data"