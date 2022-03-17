from rest_framework import serializers
from testing.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['Entries', 'Type', 'Title']
