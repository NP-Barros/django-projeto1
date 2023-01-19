from django.urls import path

from . import views  # O ponto é para falar que está na mesma pasta

app_name = 'recipes'

urlpatterns = [

    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
