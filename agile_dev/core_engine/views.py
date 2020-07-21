from rest_framework import permissions
from .models import ContextValues
from rest_framework import generics
from .models import ContextPrinciple
from .serializers import ValuesSerializer
from .serializers import PrincipleSerializer
# Create your views here.


class ListValues(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = ContextValues.objects.all()
    serializer_class = ValuesSerializer


class ListValuesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ValuesSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = self.model.objects.filter(id=id)
        return queryset

    def get_object(self):
        return self.model.objects.get(id=self.kwargs['id'])


class ListPrinciple(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = ContextPrinciple.objects.all()
    serializer_class = PrincipleSerializer


class ListPrincipleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PrincipleSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = self.model.objects.filter(id=id)
        return queryset

    def get_object(self):
        return self.model.objects.get(id=self.kwargs['id'])
