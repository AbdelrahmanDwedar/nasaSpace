from django.shortcuts import render
from recommendations.models import Recommendation

# Create your views here.
def home(request):
    return render(request, "template/index.html", {Recommendation})
