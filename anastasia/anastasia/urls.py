from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from main.views import ProductView
from main.views import CarritoView
from payments.views import BuyView
import main
import payments


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('carrito/', CarritoView.as_view(),name='carrito'),
    path('bolsas/<str:sku>/', ProductView.as_view(),name='producto'),
    path('add_to_car/<str:slug>/', main.views.add_to_car,name='add_to_car'),
    path('switch_to_len/', main.views.switch_to_len,name='switch_to_len'),
    path('instagram/', main.views.instagram,name='instagram'),
    path('set_new_value_to_car/<str:slug>/', main.views.set_new_value_to_car,name='set_new_value_to_car'),
    path('quit_to_car/<str:slug>/', main.views.quit_to_car,name='quit_to_car'),
    path('like/<str:slug>/', main.views.like,name='like'),
    path('buy/',  BuyView.as_view(),name='buy'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

