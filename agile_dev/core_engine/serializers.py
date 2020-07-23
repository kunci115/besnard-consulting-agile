from rest_framework import serializers
from .models import ContextValues
from .models import ContextPrinciple


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextValues
        fields = ["id", "title", "values_desc"]


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextPrinciple
        fields = ["id", "title", "principles_desc"]
