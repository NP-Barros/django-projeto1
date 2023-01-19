from django.urls import path

from recipes.views import home

from . import views  # O ponto é para falar que está na mesma pasta

urlpatterns = [
    path('', home),
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
