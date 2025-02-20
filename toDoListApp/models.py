from django.db import models
import uuid
# Create your models here.
class Task(models.Model):
    id = models.UUIDField( default=uuid.uuid4, editable=False, primary_key=True)
    nameTask = models.CharField(max_length=200)
    description = models.TextField()
    dateCreation= models.DateField(auto_now_add=True)