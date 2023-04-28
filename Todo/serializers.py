from rest_framework import serializers
from .models import TodoList


class todolistserializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"
