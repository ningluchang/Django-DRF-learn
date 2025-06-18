from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .models import Book
from .serializer import BookSerializer
from .permission import IsOwnerOrReadOnly
from .filters import BookFilter
from rest_framework import generics,status
from rest_framework.response import Response
from .serializer import RegisterSerializer
from django.contrib.auth.models import User


class BookController(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_class = BookFilter

    ordering_fields = ['title','price']
    search_fields = ['title']

    def perform_create(self, serializer):
        # 新增book时自动设置当前用户为作者
        serializer.save(author=self.request.user)

class RegisterController(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer