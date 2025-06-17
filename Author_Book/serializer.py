from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','name']

class BookSerializer(serializers.ModelSerializer):
    # 新增时传入作者的ID
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id','title','author']

class AuthorDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # 嵌套书籍序列化器

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']