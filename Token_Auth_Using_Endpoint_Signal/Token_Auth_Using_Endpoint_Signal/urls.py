from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Objects
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentModelViewSet,basename = 'student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',
    namespace='rest_framework')),
    path('token/', obtain_auth_token)
]
