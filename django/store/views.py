from django.urls.conf import include
from store import serializers
from store.serializers import ProductSerializer, CategorySerializer
from store.models import Product
from django.shortcuts import render
from rest_framework import generics

from .models import Category, Product
from store import models

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return models.Product.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs["slug"]).get_descendants(include_self=True)
        )

class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.filter(level=0)
    serializer_class = CategorySerializer







