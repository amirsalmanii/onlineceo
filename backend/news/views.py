from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import filters
from .models import News
from .serializers import NewsSerializer, NewsSerializer2
from accounts.views import MyPagination


class ListNewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__first_name', 'body']


class ListNews2View(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CreateNewsView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer2


class UpdateNewsView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer2


class DetailDeleteView(RetrieveDestroyAPIView):
    """
    request get ==> give news details
    request delete ==> delete news
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LastThreeNews(ListAPIView):
    serializer_class = NewsSerializer2
    def get_queryset(self):
        queryset = News.objects.all()[:3]
        return queryset