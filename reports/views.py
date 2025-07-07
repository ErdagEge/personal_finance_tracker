from django.shortcuts import render
from transactions.models import Transaction
import pandas as pd
import plotly.express as px
from django.contrib.auth.decorators import login_required

@login_required
def reports_dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)

    if not transactions.exists():
        return render(request, 'reports/dashboard.html', {'no_data': True})

    # convert to DataFrame
    data = pd.DataFrame(list(transactions.values()))
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)

    # spending over time
    expense_data = data[data['transaction_type'] == 'EXPENSE']
    expense_by_date = expense_data.groupby('date')['amount'].sum().reset_index()

    fig = px.line(expense_by_date, x='date', y='amount', title='Expenses Over Time')
    chart_html = fig.to_html(full_html=False)

    # category breakdown
    category_breakdown = expense_data.groupby('category_id')['amount'].sum()
    category_breakdown = category_breakdown.to_dict()

    return render(request, 'reports/dashboard.html', {
        'chart': chart_html,
        'category_breakdown': category_breakdown,
        'no_data': False
    })
