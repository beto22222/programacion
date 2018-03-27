from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from main.views import ProductView
from main.views import CarritoView
from main import views


urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('carrito/', CarritoView.as_view(),name='carrito'),
    path('bolsas/<str:sku>/', ProductView.as_view(),name='producto'),
    path('add_to_car/<str:slug>/', views.add_to_car,name='add_to_car'),
    path('switch_to_len/', views.switch_to_len,name='switch_to_len'),
    path('instagram/', views.instagram,name='instagram'),
    path('set_new_value_to_car/<str:slug>/', views.set_new_value_to_car,name='set_new_value_to_car'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

