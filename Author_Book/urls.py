from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import AuthorController,BookController

router = DefaultRouter()
router.register(r'author', AuthorController)
router.register(r'book', BookController)

urlpatterns = [
    path('', include(router.urls))
]