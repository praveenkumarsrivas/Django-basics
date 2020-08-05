from django.db import models

# Create your models here.
class Feedback(models.Model):
    name= models.CharField(max_length=30)
    number=models.CharField(max_length=20)
    email= models.CharField(max_length=30)
    rate=models.CharField(max_length=2)
    suggestion= models.TextField()
    best=models.TextField()
    worst = models.TextField()
    def __str__(self):
        return self.name