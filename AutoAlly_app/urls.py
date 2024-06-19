from .views import CarView, CarBrandsView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cars/', CarView.as_view(), name='car-list'),
    path('cars/<str:vin>/', CarView.as_view(), name='car-detail'),
    path('cars/brands/', CarBrandsView.as_view(), name='car-brands'),  # Nowa ścieżka dla marek samochodów
    path('admin/', admin.site.urls),
    path('api/', include('AutoAlly_app.urls.py'))
]
