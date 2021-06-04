from budget.models import Project, Category, Expense
import pytest
from django.test import TestCase

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestModels,cls).setUpClass()
        cls.project1=Project.objects.create(
            name='project-1',
            budget=10000
        )

    def test_project_is_assigned_slug(self):
        assert self.project1.slug == 'project-1'

    def test_left_budget(self):
        self.category1 = Category.objects.create(
            project = self.project1,
            name = 'development'
        )

        Expense.objects.create(
            project = self.project1,
            title = 'expense1',
            amount = 5000,
            category = self.category1
        )

        Expense.objects.create(
            project = self.project1,
            title = 'expense2',
            amount = 3000,
            category = self.category1
        )

        assert self.project1.budget_left == 2000

    def test_total_trans(self):
        self.project2 = Project.objects.create(
            name = 'project2',
            budget = 10000
        )

        self.category1 = Category.objects.create(
            project = self.project2,
            name = 'development'
        )

        Expense.objects.create(
            project = self.project2,
            title = 'expense1',
            amount = 5000,
            category = self.category1
        )

        Expense.objects.create(
            project = self.project2,
            title = 'expense2',
            amount = 3000,
            category = self.category1
        )

        assert self.project2.total_transactions == 2
