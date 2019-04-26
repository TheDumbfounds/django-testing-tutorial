from django.test import TestCase
from budget.forms import ExpenseForm


class TestForms(TestCase):

    def test_expenseform_with_data(self):
        form_data = {
            "title" : "expense_one",
            "amount" : "100",
            "category" : "development",

        }

        form = ExpenseForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)


    def test_expenseform_with_no_data(self):
        form_data = {}

        form = ExpenseForm(form_data)

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)