from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f"{self.title} "
                f"by {self.author} "
                f"at {self.created_at}")

class Lesson(models.Model):
    week_id = models.IntegerField()
    day_of_week = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    is_cancelled = models.BooleanField(default=False)
    
    teacher = models.CharField(max_length=100, blank=True, null=True)
    classroom = models.CharField(max_length=20, blank=True, null=True)
    time_slot = models.CharField(max_length=50, blank=True, null=True)  
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        status = "Скасовано" if self.is_cancelled else "Активний"
        return f"Тиждень {self.week_id} | {self.day_of_week} | {self.name} ({status})"