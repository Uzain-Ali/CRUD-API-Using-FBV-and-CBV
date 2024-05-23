from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

    class Meta:
        db_table = "paginated_student_data"