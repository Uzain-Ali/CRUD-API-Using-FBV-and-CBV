
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crudapi/', views.StudentLCAPI.as_view()),
    path('crudapi/<int:pk>/', views.StudentRUDAPI.as_view()),
]
