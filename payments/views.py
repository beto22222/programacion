from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
import json
from django.views.generic import TemplateView
import requests 
from django.views.decorators.csrf import csrf_protect
from main.models import Product


from payments.models import Sale


class BuyView(TemplateView):
    template_name='main/buy.html'

    def get_context_data(self,*args,**kwargs):

        end_cost=10

        p=self.request.session.get('objects_oncar')
        descriptions=" "
        if len(p):
	        for i in p:
	            descriptions=Product.objects.get(slug = i[0]).description_en

        print(descriptions)

        data = {}
        txnid = get_transaction_id()
        hash_ = generate_hash(self.request, txnid)
        hash_string = get_hash_string(self.request, txnid)
        # use constants file to store constant values.
        # use test URL for testing
        data["action"] = constants.PAYMENT_URL_LIVE 
        data["amount"] = float(constants.PAID_FEE_AMOUNT)
        data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
        data["key"] = constants.KEY
        data["txnid"] = txnid
        data["hash"] = hash_
        data["hash_string"] = hash_string
        '''
        data["firstname"] = "Alberto"
        data["email"] = "albeam12350@hola.com"
        data["phone"] = "5513584608"
        '''
        data["service_provider"] = constants.SERVICE_PROVIDER
        data["furl"] = self.request.build_absolute_uri(reverse("carrito"))
        data["surl"] = self.request.build_absolute_uri(reverse("inicio"))

        return (data)

def payment_success(request):
	h=0
def payment_failure(request):
	h=0

      

@csrf_protect
def pay(request):
    if request.method == 'GET':
        return render(request, 'main/buy.html')
    else:
        token_id = request.POST["conektaTokenId"]
        sale = Sale()
        if token_id: #Prevents send empty token
            return HttpResponse(sale.charge())





