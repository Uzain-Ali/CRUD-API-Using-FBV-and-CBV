
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('curdapi/', views.StudentList.as_view()),
    # path('curdapi/', views.StudentCreate.as_view()),
    # path('curdapi/<int:pk>', views.StudentRetrieve.as_view()),
    path('curdapi/<int:pk>', views.StudentDestroy.as_view()),
    path('curdapi/<int:pk>', views.StudentUpdate.as_view()),
]
