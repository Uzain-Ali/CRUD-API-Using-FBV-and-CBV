from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter


# Create router object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentROMVS,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
