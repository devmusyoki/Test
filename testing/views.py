from rest_framework import generics
from testing.models import Category
from .Serializers import CategorySerializer


class SidebarList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pass


class SidebarDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pass
