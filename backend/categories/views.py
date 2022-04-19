from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView
)
from . import (
    models,
    serializers
)


class ListCategories(ListAPIView):
    """
    Gives parent categories with their childeren
    good for navbar and etc
    """
    queryset = models.Category.objects.filter(parent__isnull=True)
    serializer_class = serializers.CategoriesSerializer


class ListCategories2(ListAPIView):
    """
    gives all categories
    good for admin panel
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer


class ListCategories3(ListAPIView):
    """
    Gives parent categories with their childeren
    good for navbar and etc
    """
    queryset = models.Category.objects.filter(parent__isnull=True)
    serializer_class = serializers.CategoriesUpdateSerializer


class DetailDeleteUpdateCategory(APIView):
    """"
    request get ==> detail of category
    request delete ==> delete category
    request put ==> update category
    """

    def get(self, request, pk):
        category = get_object_or_404(models.Category, id=pk)
        serializer = serializers.CategoriesUpdateSerializer(category)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        category = get_object_or_404(models.Category, id=pk)
        category.delete()
        return Response(status=204)

    def put(self, request, pk):
        print(request.data)
        category = get_object_or_404(models.Category, id=pk)
        serializer = serializers.CategoriesUpdateSerializer(data=request.data, instance=category)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)

