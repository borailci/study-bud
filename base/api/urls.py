from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom),
]
# kızarkadaşımın 