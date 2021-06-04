from budget.forms import ExpenseForm

class TestForms:

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
