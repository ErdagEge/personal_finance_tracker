from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.transaction_type})"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField(help_text="Use first day of the month, e.g. 2025-07-01")

    class Meta:
        unique_together = ('user', 'category', 'month')

    def __str__(self):
        return f"{self.user} | {self.category} | {self.month} | {self.amount}"
