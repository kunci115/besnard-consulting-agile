import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_values_all(client):
   url = reverse('list-values')
   response = client.get(url)
   assert response.status_code == 200