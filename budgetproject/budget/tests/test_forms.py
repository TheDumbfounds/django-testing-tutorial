from budget.forms import ExpenseForm
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestForms(TestCase):

    def test_valid_data(self):
        form =ExpenseForm(data={
            'title' : 'expense1',
            'amount' : 1000,
            'category' : 'deployment'
        })

        assert form.is_valid() == True

    def test_not_valid_data(self):
        form =ExpenseForm(data={})

        assert form.is_valid() == False
        assert len(form.errors) == 3
