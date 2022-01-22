from django.contrib.auth.models import User
from rest_framework import viewsets
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from blog.models import Category, Article
from blog.serializers import CategorySerializer, ArticleSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        try:
            return self.queryset
        finally:
            print(f'QUERY::: {connection.queries}')

    @method_decorator(cache_page(60*1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)