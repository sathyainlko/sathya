from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project

# Create your views here.

def home(request):

	projects = Project.objects.all()

	return render(request, 'home.html', {'projects': projects})
