from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('curdapi/', views.student_api),
    path('curdapi/<int:pk>', views.student_api)
]
