from django.urls import path, re_path
from .views import (
    ListValues,
    ListPrinciple,
    ListPrincipleDetailAPIView,
    ListValuesDetailAPIView
)

urlpatterns = [
    path('values/all/', ListValues.as_view(), name='list-values'),
    path('principle/all/', ListPrinciple.as_view(), name='list-values'),
    re_path(r'values/(?P<id>\d+)/$', ListValuesDetailAPIView.as_view(), name='list-values'),
    re_path(r'principle/(?P<id>\d+)/$', ListPrincipleDetailAPIView.as_view(), name='list-values'),
]
