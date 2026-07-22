from django.db import models
from django.conf import settings
# Create your models here.

class BirthChart(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE,
                           null=True,
                           blank=True
                           )
    
    full_name=models.CharField(max_length=100,
                               blank=True,
                               null=True)
    
    date_of_birth=models.DateField()

    time_of_birth=models.TimeField()

    place_of_birth=models.CharField(max_length=255)

    gender=models.CharField(max_length=20,
                            blank=True,
                            null=True)
    
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.full_name:
            return self.full_name
        return f"Kundali {self.id}"
    
class AstrologyQuestion(models.Model):
    question=models.CharField(max_length=255)

    answer=models.TextField()

    is_active=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
    
