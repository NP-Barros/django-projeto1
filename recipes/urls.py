from django.urls import path

from . import views  # O ponto é para falar que está na mesma pasta

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
