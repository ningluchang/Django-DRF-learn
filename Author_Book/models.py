from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,related_name='books', on_delete=models.CASCADE)
    # 价格字段
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
