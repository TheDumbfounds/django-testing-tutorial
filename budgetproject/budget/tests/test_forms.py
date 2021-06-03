from budget.forms import ExpenseForm

class TestForms:

    def test_valid_data(self):
        form =ExpenseForm(data={
            'title' : 'expense1',
            'amount' : 1000,
            'category' : 'deployment'
        })

        assert form.is_valid() == True
