from django.shortcuts import render, redirect
from .models import Transaction, Category, Budget
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'transactions/budget_list.html', {'budgets': budgets})

@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'transactions/add_budget.html', {'form': form})


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})
