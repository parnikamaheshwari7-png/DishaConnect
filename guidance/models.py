from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(
        max_length=100,
        unique=True
    )

    description=models.TextField(blank=True)

    def __str__(self):
        return self.category_name
    
class Question(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_title=models.CharField(max_length=255)
    
    answer=models.TextField()
    
    is_active=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_title
