from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import categories,technologies,colors,countries,Project,Profile,Rating
from .forms import ProjectForm,ProfileForm,RatingForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.db.models import Max
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer,technologiesSerializer,colorsSerializer,countriesSerializer,categoriesSerializer


# Create your views here.
def index(request):
    date = dt.date.today()
    winners=Project.objects.all()[:4]
    caraousel = Project.objects.order_by('-overall_score')[0]
    nominees=Project.objects.all()[4:8]
    directories=Project.objects.all()[8:11]
    resources=Project.objects.all()[11:15]
    resources2=Project.objects.all()[15:19]

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(username=current_user)
        print(current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date,"nominees":nominees,"directories":directories,"resources":resources,"resources2":resources2})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.avatar = profile.avatar
            project.country = profile.country

            project.save()
    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})