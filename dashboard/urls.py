from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('produtos/', views.produtos, name='produtos'),
    path('estoque/', views.estoque, name='estoque'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)