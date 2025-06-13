from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterController,CustomObtainAuthToken

# DefaultRouter会自动审查标准的REST ful接口路径与方法映射
router = DefaultRouter()
# router.register(r'user', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('register/', RegisterController.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),

]
