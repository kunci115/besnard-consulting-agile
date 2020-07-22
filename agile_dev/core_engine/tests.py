import pytest
from django.urls import reverse
import json

def create_values(client):
    r = client.post('/api/values/all/',
        {
        "title": "Individuals and interactions",
        "values_desc": "In the past, a lot of software teams would concentrate on having the best possible tools or processes with which to build their software. The Agile Manifesto suggests that while those things are important, the people behind the processes are even more so.Having the right group of individuals on your software team is vital to success. The best possible tools in the wrong hands are worthless. Perhaps even more important is how these individuals communicate with each other. The interactions between team members are what helps them to collaborate and solve any problems that arise."
    }, format='json')

    return r


def put_values(client, id):
    r = client.put('/api/values/{}/'.format(id),
        {
        "title": "Customer collaboration",
        "values_desc": "Once upon a time, contracts were king. You would draw up contracts with your customers who would then detail the finished product. As a result, there was often a contrast between what the contract said, what the product did, and what the customer actually required. According to the Agile Manifesto, the focus should be on continuous development. You need to build a feedback loop with your customers so that you can constantly ensure that your product works for them."
    }, format='json')

    return r


def delete_values(client, id):
    r = client.delete('/api/values/{}/'.format(id),
        {
            "id": id
        }, format='json')

    return r


def get_all_values(client):
    r = client.get('/api/values/all/',format='json')
    return json.loads(r.content)


@pytest.mark.django_db()
def test_add_new_values(api_client):
    r = create_values(api_client)

    assert r.status_code == 201


@pytest.mark.django_db()
def test_get_values_all(api_client):
    create_values(api_client)
    r = get_all_values(api_client)
    assert len(r) == 2


@pytest.mark.django_db()
def test_put_values(api_client):
    all_values = get_all_values(api_client)
    values_id = all_values[0]['id']
    r = put_values(api_client, id=values_id)
    new_values = json.loads(r.content)
    assert r.status_code == 200
    assert new_values['title'] == "Customer collaboration"


@pytest.mark.django_db()
def test_delete_values(api_client):
    all_values = get_all_values(api_client)
    values_id = all_values[0]['id']
    r = delete_values(api_client, id=values_id)
    assert r.status_code == 204


def create_principles(client):
    r = client.post('/api/principle/all/',
        {
        "title": "Satisfy the Customer",
        "values_desc": "Business people and developers must work together daily throughout the project. It makes sense for the customer to become part of the team.  After all, both the developers and the customers have the same goal; to deliver valuable software."
    }, format='json')

    return r
