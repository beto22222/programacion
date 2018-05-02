from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Product,User,Data
import json
from django.views.generic import TemplateView
import requests 
import smtplib


class CarritoView(TemplateView):
    template_name='main/carrito.html'
    def get_context_data(self,*args,**kwargs):
        check(self.request)
        p=self.request.session.get('objects_oncar')

        products=[]
        end_cost=0
        if len(p):
            for i in p:
                d=Product.objects.get(slug = i[0])
                end_cost+=d.price*i[1]
                d.qty=i[1]
                products.append(d)
        set_end_cost(self.request,end_cost)
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
        print('-----------------------------data----------------------------------------------')
        if Data.objects.filter(ip=self.request.META['REMOTE_ADDR']):
            print('ya esta aqui')
        else:
            print('nuevo')
            data = Data(ip=self.request.META['REMOTE_ADDR'],data=self.request.META)
            data.save()
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

class InspiringSpotlightView(TemplateView):

    template_name='main/inspiring_spotlight.html'
    
class ContactUsView(TemplateView):

    template_name='main/contact_us.html'

class BuyView(TemplateView):
    template_name='main/buy.html'
    def get_context_data(self,*args,**kwargs):
        check(self.request)
        p=self.request.session.get('objects_oncar')

        products=[]
        end_cost=0

        if len(p):
            for i in p:
                d=Product.objects.get(slug = i[0])
                end_cost+=d.price*i[1]
        context = {
            'end_cost':end_cost
        }

        set_end_cost(request,end_cost)
        return (context)

def add_to_car(request,slug):
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

    return(HttpResponseRedirect('/'))

def quit_to_car(request,slug):
    
    data=request.session.get('objects_oncar')
    clasif=list(map(lambda x: slug in x,data))
    if True in clasif:
        del data[clasif.index(True)]
    request.session['objects_oncar']=data
    
    end_cost=0

    if len(data):
        for i in data:
            d=Product.objects.get(slug = i[0])
            end_cost+=d.price*i[1]
    context = {
        'end_cost':str(end_cost)
    }

    set_end_cost(request,end_cost)
    return(HttpResponse(json.dumps(context),content_type='application/json'))

def like(request,slug):
    obj = Product.objects.get(slug=slug)
    obj.punctuation =obj.punctuation+1
    obj.save()
    
    context = {
        'punctuation':str(obj.punctuation),
    }
    return(HttpResponse(json.dumps(context),content_type='application/json'))

def set_new_value_to_car(request,slug):
    
    if request.session.get('objects_oncar')==None:
        request.session['objects_oncar']=[]
    data=request.session.get('objects_oncar')
    clasif=list(map(lambda x: slug in x,data))

    if True in clasif:
        if int(request.GET['value'])>0:        
            data[clasif.index(True)][1]=int(request.GET['value'])

    request.session['objects_oncar']=data

    p=request.session.get('objects_oncar')

    end_cost=0

    if len(p):
        for i in p:
            d=Product.objects.get(slug = i[0])
            end_cost+=d.price*i[1]
    context = {
        'end_cost':str(end_cost)
    }

    set_end_cost(request,end_cost)
    return(HttpResponse(json.dumps(context),content_type='application/json'))

def switch_to_len(request):
    if request.GET['len']=='len_en':
        request.session['lang'] = 'en'
    else:
        request.session['lang'] = 'es'
    a=request.GET['i']
    return(HttpResponseRedirect('/'))

def instagram(request):
    template = loader.get_template('main/instagram.html')
    r = requests.get('https://snapwidget.com/embed/527909')

    
    r=r.text.replace('a href','a href="https://www.instagram.com/anastasiaecothique/" name')
    context = {'pag':r.replace('width="100%"','')}

    return HttpResponse(template.render(context, request))

def check(request):
    if request.session.get('objects_oncar')==None:
        request.session['objects_oncar']=[]

    if request.session.get('lang')==None:
        request.session['lang']='es'

def set_end_cost(request,end_cost):

    request.session['end_cost']=str(end_cost)

def send_email(request):

    print("----------------------------------------------")
    
    msg = request.GET.get('name') + " > " + request.GET.get('email') + " dice: " + request.GET.get('content')
    print(msg)
    print("mensaje enviado")
    fromaddr = 'alberto.moca12350@gmail.com'
    toaddrs  = 'alberto.moca12350@gmail.com'
     
    # Datos
    username = 'alberto.moca12350@gmail.com'
    password = 'elhijodelinternet'
     
    # Enviando el correo
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)


    
 
    BODY = '\r\n'.join(['To: %s' % toaddrs,
                    'From: %s' % fromaddr,
                    'Subject: %s' % "SUBJECT",
                    '', msg])
    
    server.sendmail(fromaddr, toaddrs, BODY)
    create_or_update_user(request)
    server.quit()

    return(HttpResponseRedirect('/'))


def create_or_update_user(request):
    if User.objects.filter(email=request.GET.get('email')):
        User.objects.filter(email=request.GET.get('email')).update(name=request.GET.get('name'))
        print('ya esta aqui')
    else:
        print('nuevo')
        user = User(name=request.GET.get('name'), email=request.GET.get('email'))
        user.save()



def suscribe_to_newsletter(request):
    print('llego')
    if User.objects.filter(email=request.GET.get('email')):
        print('ya esta aqui')
    else:
        
        user = User(email=request.GET.get('email'))
        user.save()

    return(HttpResponseRedirect('/'))

