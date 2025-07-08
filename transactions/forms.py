from django import forms
from .models import Transaction
from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'month']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'transaction_type', 'description', 'date']
