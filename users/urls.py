from django.urls import path
from . import views
# O ponto acima significa que está acessando a pasta atual
urlpatterns = [
    path('registro/', views.register, name='register'),
]
#path('registro/', views.register, name='register'),