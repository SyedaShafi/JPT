from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', views.ClientViewset)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('signup/', views.UserRegistrationAPIView.as_view(), name='signup'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
]