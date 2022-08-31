from rest_framework import viewsets
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from admin_panel.models import News
from admin_panel.serializers import NewsSerializer


class CursorSetPagination(CursorPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    ordering = '-created_at'


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = CursorSetPagination
