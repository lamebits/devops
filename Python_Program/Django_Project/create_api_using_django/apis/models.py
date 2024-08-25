from django.db import models

# Create your models here.
class ApiModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.title