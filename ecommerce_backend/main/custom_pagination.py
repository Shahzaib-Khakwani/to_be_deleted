from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):

    page_size = None
    allow_empty = True
