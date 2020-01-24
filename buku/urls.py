from django.urls import  path
# Create your views here.

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:buku_id>/', views.detail, name='detail'),

]