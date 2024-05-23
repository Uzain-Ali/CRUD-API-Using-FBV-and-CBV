from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


    class Meta:
        db_table = "singer"

        
    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()
     

    class Meta:
        db_table = "song"

    def __str__(self):
        return self.title
    
