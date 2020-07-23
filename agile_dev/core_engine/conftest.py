import pytest
import base64

from django.contrib.auth.models import User

from .models import ContextValues, ContextPrinciple

@pytest.fixture(autouse=True)
def add_user():
    m = User.objects.create(email="kunci115@gmail.com", password="123besnard123", username="kunci115")


@pytest.fixture(autouse=True)
def api_client():
    from rest_framework.test import APIClient
    credentials = base64.b64encode(f'{"kunci11"}:{"123besnard123"}'.encode('utf-8'))
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(credentials.decode('utf-8')))
    return client


@pytest.fixture(autouse=True)
def add_default_value_context():
    c = ContextValues.objects.create(
        title="Working Software Over Comprehensive Documentation 1",
        values_desc="Historically, enormous amounts of time were spent on documenting the product for development and ultimate delivery. Technical specifications, technical requirements, technical prospectus, interface design documents, test plans, documentation plans, and approvals required for each. The list was extensive and was a cause for the long delays in development. Agile does not eliminate documentation, but it streamlines it in a form that gives the developer what is needed to do the work without getting bogged down in minutiae. Agile documents requirements as user stories, which are sufficient for a software developer to begin the task of building a new function.\nThe Agile Manifesto values documentation, but it values working software more.",
    )


@pytest.fixture(autouse=True)
def add_default_principle():
    c = ContextPrinciple.objects.create(
        title="Deliver Frequently",
        principles_desc="Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale. The sooner you deliver incremental software, the faster the feedback and faster you can identify a wrong turn or a miscommunication with the client.  Would you rather find out earlier when you can do something about it or at the end when a complete rework is required?",
    )
