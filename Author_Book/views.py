from rest_framework import viewsets
from .models import Author,Book
from .serializer import AuthorSerializer,BookSerializer,AuthorDetailSerializer

class AuthorController(viewsets.ModelViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AuthorDetailSerializer
        return AuthorSerializer

class BookController(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
