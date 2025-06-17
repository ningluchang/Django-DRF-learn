# 自定义分页

from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    # 每页默认返回5条
    page_size = 5
    # 客户端可以用?page_size=3指定每页返回的记录数
    page_size_query_param = 'page_size'
    # 限制最大每页100条
    max_page_size = 100