import pytest
from .models import ContextValues


@pytest.fixture(autouse=True)
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture(autouse=True)
def add_default_value():
    c = ContextValues.objects.create(
        title = "Working Software Over Comprehensive Documentation 1",
        values_desc="Historically, enormous amounts of time were spent on documenting the product for development and ultimate delivery. Technical specifications, technical requirements, technical prospectus, interface design documents, test plans, documentation plans, and approvals required for each. The list was extensive and was a cause for the long delays in development. Agile does not eliminate documentation, but it streamlines it in a form that gives the developer what is needed to do the work without getting bogged down in minutiae. Agile documents requirements as user stories, which are sufficient for a software developer to begin the task of building a new function.\nThe Agile Manifesto values documentation, but it values working software more."
    )

