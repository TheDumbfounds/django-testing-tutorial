from budget.models import Project, Category, Expense
import pytest
from django.test import TestCase

class TestModels(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestModels,cls).setUpClass()
        cls.project1=Project.objects.create(
            name='project-1',
            budget=1000
        )

    def test_project_is_assigned_slug(self):
        assert self.project1.slug == 'project-1'
