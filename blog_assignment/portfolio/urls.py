from django.urls import path
from . import views
    
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:port_id>', views.detailport, name='detailport'),
    path('newport/', views.newport, name='newport'),
    path('createport/', views.createport, name='createport'),
]