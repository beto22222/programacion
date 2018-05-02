from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from main.views import ProductView,CarritoView,InspiringSpotlightView,ContactUsView,IndexView
import main
import payments.views

 
urlpatterns = [
    path('',IndexView.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('carrito/', CarritoView.as_view(),name='carrito'),
    path('bolsas/<str:sku>/', ProductView.as_view(),name='producto'),
    path('add_to_car/<str:slug>/', main.views.add_to_car,name='add_to_car'),
    path('switch_to_len/', main.views.switch_to_len,name='switch_to_len'),
    path('instagram/', main.views.instagram,name='instagram'),
    path('set_new_value_to_car/<str:slug>/', main.views.set_new_value_to_car,name='set_new_value_to_car'),
    path('quit_to_car/<str:slug>/', main.views.quit_to_car,name='quit_to_car'),
    path('like/<str:slug>/', main.views.like,name='like'),
    path('comprar/',  payments.views.pay , name='comprar'),
    path('datos_de_envio/',  payments.views.datos_de_compra , name='datos_de_compra'),
    path('inspiring_spotlight/',  InspiringSpotlightView.as_view(),name='inspiring_spotlight'),
    path('contact_us/', ContactUsView.as_view(),name='contact_us'),
    path('send_email/', main.views.send_email,name='send_email'),
    path('suscribe_to_newsletter/', main.views.suscribe_to_newsletter,name='suscribe_to_newsletter'),
   # path('comprar/success', payment.views.payment_success, name="payment_success"),
    #path('comprar/failure', payment.views.payment_failure, name="payment_failure"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


