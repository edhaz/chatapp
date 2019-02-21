from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:chatter_name>/', views.detail, name='detail'),
    path('<str:chatter_name>/results/', views.results, name='results'),
    path('<str:chatter_name>/vote/', views.vote, name='vote')
]
