from rest_framework import viewsets
from .models import Author,Book
from .serializer import AuthorSerializer,BookSerializer,AuthorDetailSerializer
from .pagination import MyPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from .filter import BookFilter

class AuthorController(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer

class BookController(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # 分页器
    pagination_class = MyPageNumberPagination
    # 注册了多个过滤类（Filter Backend）。它定义了该视图集支持的过滤、排序、搜索等“过滤器”的组合。
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    # 指定自定义过滤器
    filterset_class = BookFilter

    # 根据作者查询
    # filterset_fields = ['author']
    # 支持按title排序
    ordering_fields = ['title']
    # 支持title模糊查询
    search_fields = ['title']
