from django.db import models
from django.db.backends.utils import time
from users.models import User

# Create your models here.
class Recommendation(models.Model):
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
