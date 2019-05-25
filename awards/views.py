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
