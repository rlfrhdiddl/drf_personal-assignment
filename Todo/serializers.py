from rest_framework import serializers
from .models import TdList


class todolistserializer(serializers.ModelSerializer):
    class Meta:
        model = TdList
        fields = "__all__"
