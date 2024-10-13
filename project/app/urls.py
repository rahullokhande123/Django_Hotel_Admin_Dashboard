from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('query/', views.query, name='query'),
    path('querydata/<int:x>', views.querydata, name='querydata')
]