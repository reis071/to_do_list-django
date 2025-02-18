from django.urls import path
from . import views

urlpatterns = [
    path('registerTask/', views.addTask, name='registerTask'),
]