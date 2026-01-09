from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),
    # API endpoints for React frontend
    path('api/shorten/', views.api_shorten, name='api_shorten'),
    path('api/generate-qr/', views.api_generate_qr, name='api_generate_qr'),
    path('api/recent/', views.api_recent, name='api_recent'),
    path('s/<str:code>/', views.redirect_short, name='redirect_short'),
    path('qr/<str:code>/', views.qr_code, name='qr_code'),
]
