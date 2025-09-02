from django.contrib import admin
from django.urls import path
from . import views

<<<<<<< HEAD

urlpatterns = [
    path('', views.inicio, name='home'),
    path('data-hora/', views.verDataHora, name='agora'),
]


=======
urlpatterns = [
    path('', views.inicio),
    path('data-hora/', views.verDataHora),
]
>>>>>>> 84b50a04211a476323ea55508ad13ae40518e90a
