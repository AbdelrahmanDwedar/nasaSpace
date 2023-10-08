from django.db import models as db
from django.contrib.auth import models


# Create your models here.
class User(models.User):
    prefix = db.CharField(max_length=5, blank=True)
    mid_name = db.CharField(max_length=2, blank=True)
    role = db.CharField(max_length=120, blank=True)

    REQUIRED_FIELDS = ["email", "username"]
