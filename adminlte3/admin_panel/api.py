from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from admin_panel.models import News
from admin_panel.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)