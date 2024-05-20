from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('curdapi/', views.StudentRetrieveUpdateDestroy.as_view()),
    path('curdapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view())
]
