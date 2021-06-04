from django.test import Client
from django.urls import reverse
from budget.models import Project, Category, Expense
import json
import pytest
from django.test import TestCase

@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews,cls).setUpClass()
        cls.client = Client()
        cls.list_url = reverse('list')
        cls.detail_url = reverse('detail',kwargs={'project_slug':'project1'})
        cls.project1 = Project.objects.create(
            name = 'project1',
            budget = 10000
        )

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        assert response.status_code == 200
        assert 'budget/project-list.html' in (t.name for t in response.templates)

    def test_project_details_GET(self):
        response = self.client.get(self.detail_url)

        assert response.status_code == 200
        assert 'budget/project-detail.html' in (t.name for t in response.templates)

    def test_project_list_POST_add(self):
        Category.objects.create(
            project=self.project1,
            name = 'development'
        )

        response = self.client.post(self.detail_url,{
            'title' : 'expense1',
            'amount' : 1000,
            'category' : 'development'
        })

        assert response.status_code == 302
        assert self.project1.expenses.first().title == 'expense1'

    def test_project_list_POST_not_add(self):
        response = self.client.post(self.detail_url)

        assert response.status_code == 302
        assert self.project1.expenses.count() == 0

    def test_project_list_DELETE_expense(self):
        self.category1 = Category.objects.create(
            project = self.project1,
            name = 'development'
        )
        Expense.objects.create(
            project = self.project1,
            title = 'expense1',
            amount = 1000,
            category = self.category1
        )

        response = self.client.delete(self.detail_url,json.dumps({'id':1}))

        assert response.status_code == 204
        assert self.project1.expenses.count() == 0

    def test_project_list_DELETE_no_expense(self):
        self.category1 = Category.objects.create(
            project = self.project1,
            name = 'development'
        )
        Expense.objects.create(
            project = self.project1,
            title = 'expense1',
            amount = 1000,
            category = self.category1
        )

        response = self.client.delete(self.detail_url)

        assert response.status_code == 404
        assert self.project1.expenses.count() == 1

    def test_project_create_POST(self):
        self.create_url = reverse('add')
        response = self.client.post(self.create_url,{
            'name' : 'project2',
            'budget' : 10000,
            'categoriesString' : 'design'
        })

        project2= Project.objects.get(id=2)
        assert project2.name == 'project2'
        first_category = Category.objects.get(id=1)
        assert first_category.project == project2
        assert first_category.name == 'design'
