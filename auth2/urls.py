from django.urls import path,include
from rest_framework import routers
from .views import BookController,RegisterController
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.DefaultRouter()
router.register(r'books', BookController)
urlpatterns = [
    path('api/register/', RegisterController.as_view(), name='register'),
    path('', include(router.urls)),
    # jwt认证接口
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]