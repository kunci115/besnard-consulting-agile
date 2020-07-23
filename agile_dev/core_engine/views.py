from typing import Type, List

from rest_framework import permissions
from rest_framework.permissions import AllowAny

from .models import ContextValues
from rest_framework import generics
from .models import ContextPrinciple
from .serializers import ValuesSerializer
from .serializers import PrincipleSerializer

# Create your views here.


class ListValues(generics.ListCreateAPIView):
    permission_classes: List[Type[AllowAny]] = [permissions.AllowAny]
    queryset = ContextValues.objects.all()
    serializer_class: Type[ValuesSerializer] = ValuesSerializer


class ListValuesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes: List[Type[AllowAny]] = [permissions.AllowAny]
    serializer_class: Type[ValuesSerializer] = ValuesSerializer
    model: Type[ContextValues] = serializer_class.Meta.model

    def get_queryset(self) -> object:
        id = self.kwargs["id"]
        queryset = self.model.objects.filter(id=id)
        return queryset

    def get_object(self) -> object:
        return self.model.objects.get(id=self.kwargs["id"])


class ListPrinciple(generics.ListCreateAPIView):
    permission_classes: List[Type[AllowAny]] = [permissions.AllowAny]
    queryset = ContextPrinciple.objects.all()
    serializer_class: Type[PrincipleSerializer] = PrincipleSerializer


class ListPrincipleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes: List[Type[AllowAny]] = [permissions.AllowAny]
    serializer_class: Type[PrincipleSerializer] = PrincipleSerializer
    model: Type[ContextPrinciple] = serializer_class.Meta.model

    def get_queryset(self) -> object:
        id = self.kwargs["id"]
        queryset = self.model.objects.filter(id=id)
        return queryset

    def get_object(self) -> object:
        return self.model.objects.get(id=self.kwargs["id"])
