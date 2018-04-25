from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.shortcuts import render,redirect
import json
from django.views.generic import TemplateView
import requests 
from django.views.decorators.csrf import csrf_protect
from main.models import Product

import twocheckout
from twocheckout import TwocheckoutError


  


@csrf_protect
def datos_de_compra(request):
    if request.method == 'GET':
        context = {
            'end_cost':request.session.get('end_cost'),
            'products':request.session.get('objects_oncar')
        }
        return render(request, 'main/datos.html',context)
    else:
        request.session['usrData']={
          "name":request.POST["nam"],
          "email":request.POST["ema"],
          "street":request.POST["str"],
          "zip":request.POST["zip"],
          "country":request.POST["con"],
        }

        return HttpResponseRedirect("/comprar/")
    

@csrf_protect
def pay(request):
    datos=request.session.get('usrData')
    if request.method == 'GET':
        context = {
            'end_cost':request.session.get('end_cost'),
            'datos':datos,
            'products':request.session.get('objects_oncar')
        }
        print(request.session.get('usrData'))

        return render(request, 'main/buy.html',context)
    else:
        token_id = request.POST["token"]
        print("---------------DATOS-----------------")
        print(request.POST)
        print("--------------------------------")
        
        twocheckout.Api.auth_credentials({
            'private_key': '8C6C43F8-0B76-4BE8-B292-C5F7913B42AF',
            'seller_id': '901378287',
            'mode': 'sandbox'  #Uncomment to use Sandbox
        })
        params = {
          'merchantOrderId': '123',
          'token': token_id,
          'currency': 'USD',
          'total': request.session.get('end_cost'),
          'billingAddr': {
              'name': datos['name'],
              'addrLine1': datos['street'],
              'city': 'Columbus',
              'state': 'OH',
              'zipCode': '43123',
              'country': datos['country'],
              'email': datos['email'],
              'phoneNumber': '555-555-5555'
          }
        }
        try:
            result = twocheckout.Charge.authorize(params)
            print (result.responseCode)
            
            return render(request, 'main/exito.html')
        except TwocheckoutError as error:
            print (error.msg)
            return HttpResponse("error")

