from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('query/', views.query, name='query'),
    path('querydata/<str:x>', views.querydata, name='querydata'),
    path('delete/<int:x>/<str:y>', views.delete, name='delete'),
    path('edit/<int:x>', views.edit, name='edit'),
    path('update/', views.update, name='update') 
    
]