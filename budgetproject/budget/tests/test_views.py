from django.test import Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json
import pytest

@pytest.mark.django_db
class TestViews:

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        assert response.status_code == 200
        assert 'budget/project-list.html' in (t.name for t in response.templates)
