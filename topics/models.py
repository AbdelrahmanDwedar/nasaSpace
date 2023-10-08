from django.db import models

from users.models import User
from recommendations.models import Recommendation


# Create your models here.
class Topics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
