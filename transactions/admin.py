from django.contrib import admin
from .models import Transaction, Category
from .models import Budget

admin.site.register(Budget)
admin.site.register(Transaction)
admin.site.register(Category)
