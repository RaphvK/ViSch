from django.urls import path

from . import views

app_name = 'visch'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('betreiber/', views.betreiber_view, name='betreiber'),
    path('map/', views.map_view, name='map'),
]