from django.urls import path, re_path
from .views import ListValues, ListPrinciple, ListPrincipleDetailAPIView, ListValuesDetailAPIView

urlpatterns = [
    path('values/all/', ListValues.as_view(), name='list-values'),
    path('principle/all/', ListPrinciple.as_view(), name='list-values'),
    re_path('values/(?P<id>.+)', ListValuesDetailAPIView.as_view(), name='list-values'),
    re_path('principle/(?P<id>.+)', ListPrincipleDetailAPIView.as_view(), name='list-values'),
]
