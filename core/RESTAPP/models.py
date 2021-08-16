from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_name = models.CharField(max_length = 150)
    todo_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_name
    
