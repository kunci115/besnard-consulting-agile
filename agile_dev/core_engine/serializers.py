from rest_framework import serializers
from .models import ContextValues
from .models import ContextPrinciple


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextValues
        fields = ['title', 'values_desc']


class PrincipleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextPrinciple
        fields = ['title', 'principles_desc']
