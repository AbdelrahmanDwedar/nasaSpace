from django.shortcuts import render
from .models import User

# Create your views here.
def profile(request):
    return render(request, "template/userprofile.html", {"username":User.username})
