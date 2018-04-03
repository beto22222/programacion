from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
import json
from django.views.generic import TemplateView
import requests 


class BuyView(TemplateView):
    template_name='main/buy.html'

