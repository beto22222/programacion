from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Product
import json
from django.views.generic import TemplateView
import requests 



class CarritoView(TemplateView):
    template_name='main/carrito.html'
    def get_context_data(self,*args,**kwargs):
        check(self.request)
        p=self.request.session.get('objects_oncar')

        products=[]
        end_cost=0

        print('--------------------AQUI--------------------')
        if len(p):
            for i in p:
                d=Product.objects.get(slug = i[0])
                end_cost+=d.price*i[1]
                d.qty=i[1]
                products.append(d)
        print(end_cost)
        print('+++++++++++++++++Car++++++++++++++++++++')
        print(products)
        context = {
            'products': products,
            'end_cost':end_cost
        }
        return (context)


class IndexView(TemplateView):

    template_name='main/index.html'
    def get_context_data(self,*args,**kwargs):
        check(self.request)
        best_products = Product.objects.order_by('-id')[:30]
        context = {
            'best_products': best_products,
        }
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        print('---------------------------')
        print(ip)
        print('---------------------------')
        return (context)

class ProductView(TemplateView):
    template_name='main/product.html'
    def get_context_data(self,*args,**kwargs):
        check(self.request)
        try:
            product = Product.objects.get(name = kwargs['sku'])    
        except Product.DoesNotExist as e:
            raise Http404('No encontramos {}'.format(kwargs['sku']))

        return {'product':product,'pines':list(range(len(product.images.all())))}

def add_to_car(request,slug):
    #print(request.session.session_key)

    #print('*********************LLEGO********************************')
    #print(request.session.session_key)
    #request.session.flush()
    if request.session.get('objects_oncar')==None:
        request.session['objects_oncar']=[]
    data=request.session.get('objects_oncar')
    clasif=list(map(lambda x: slug in x,data))
    if True in clasif:
        data[clasif.index(True)][1]+=1 
    else:
        data.append([slug,1])
    request.session['objects_oncar']=data

    print('data')
    print(data)

    #print(request.session.get('objects_oncar'))
    #print('----------------------------------')

    return(HttpResponseRedirect('/'))


def quit_to_car(request,slug):
    
    data=request.session.get('objects_oncar')
    clasif=list(map(lambda x: slug in x,data))
    if True in clasif:
        del data[clasif.index(True)]
    request.session['objects_oncar']=data

    
    end_cost=0

    print('--------------------AQUI--------------------')
    if len(data):
        for i in data:
            d=Product.objects.get(slug = i[0])
            end_cost+=d.price*i[1]
    context = {
        'end_cost':str(end_cost)
    }

    return(HttpResponse(json.dumps(context),content_type='application/json'))

def like(request,slug):
    obj = Product.objects.get(slug=slug)
    obj.punctuation =obj.punctuation+1
    obj.save()
    
    context = {
        'punctuation':str(obj.punctuation),
    }
    print('-------------------')
    print(json.dumps(context))
    print('-------------------')
    return(HttpResponse(json.dumps(context),content_type='application/json'))

def set_new_value_to_car(request,slug):
    
    if request.session.get('objects_oncar')==None:
        request.session['objects_oncar']=[]
    data=request.session.get('objects_oncar')
    clasif=list(map(lambda x: slug in x,data))
    print(clasif)
    if True in clasif:
        if int(request.GET['value'])>0:        
            data[clasif.index(True)][1]=int(request.GET['value'])

    request.session['objects_oncar']=data

    p=request.session.get('objects_oncar')

    end_cost=0

    print('--------------------AQUI--------------------')
    if len(p):
        for i in p:
            d=Product.objects.get(slug = i[0])
            end_cost+=d.price*i[1]
    context = {
        'end_cost':str(end_cost)
    }
    print('-------------------')
    print(json.dumps(context))
    print('-------------------')
    return(HttpResponse(json.dumps(context),content_type='application/json'))

def switch_to_len(request):
    if request.GET['len']=='len_en':
        request.session['lang'] = 'en'
    else:
        request.session['lang'] = 'es'
    print('--------------LEN-------------------')
    print(request.session.get('lang'))
    a=request.GET['i']
    print(a)
    return(HttpResponseRedirect('/'))


def instagram(request):
    template = loader.get_template('main/instagram.html')
    r = requests.get('https://snapwidget.com/embed/527909')


    
    r=r.text.replace('width="100%"','')
    context = {'pag':r.replace('width="100%"','')}

    return HttpResponse(template.render(context, request))

def check(request):
    if request.session.get('objects_oncar')==None:
        request.session['objects_oncar']=[]

    if request.session.get('lang')==None:
        request.session['lang']='es'