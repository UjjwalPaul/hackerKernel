from django.db import models

# Create your models here.

class UserDetails (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
# class userTask (models.Model):
#     task_detail = models.TextField()
#     task_type = models.CharField(max_length=10)
#     task_email = models.EmailField(max_length=20)

class UserTask (models.Model):
    email = models.EmailField()
    pending = models.CharField(max_length=10)
    # taskdetails = models.CharField(max_length=50)
    taskdetails = models.TextField()