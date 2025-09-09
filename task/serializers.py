from rest_framework import serializers
from .models import Task
from category.serializers import CategorySerializer
from category.models import Category

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Task
        fields = ['id', 'description', 'is_completed', 'created_at', 'category', 'category_id']
