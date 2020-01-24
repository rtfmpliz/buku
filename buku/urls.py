from django.urls import  path
# Create your views here.

from . import views

app_name = 'buku'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:buku_id>/', views.detail, name='detail'),

]