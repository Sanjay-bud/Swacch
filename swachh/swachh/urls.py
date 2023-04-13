from django.urls import path,include
from . import views

formpatterns = [
    path('register/', views.user, name = 'user'),
]

urlpatterns = [
    path('swachh/', include(formpatterns)),
    path('', views.index, name = 'index'),
]


















app_name = "swachh"