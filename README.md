# Finance Tracker

Finance Tracker is a data-focused personal finance management app built with Django and Python. It allows users to:

- Record income and expenses
- Categorize transactions
- Track spending over time
- Visualize reports with interactive charts
- Securely manage their data with user accounts

This project is designed for users who want an analytical view of their finances with clean reporting and easy data handling.

---

## Features

✅ User authentication  
✅ Add / edit / delete transactions  
✅ Categorize expenses and income  
✅ Reports dashboard with Plotly charts  
✅ Simple and clean Django admin interface  

---

## Tech Stack

- **Backend**: Django, Python  
- **Data Analysis**: Pandas  
- **Data Visualization**: Plotly  
- **Database**: SQLite (dev) / PostgreSQL (production recommended)  
- **Frontend**: Django templates (optional React integration later)

---

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/finance-tracker.git
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit:
- Transactions: http://127.0.0.1:8000/transactions/
- Reports: http://127.0.0.1:8000/reports/

---

## License
MIT License. Feel free to fork and modify.

--

## Future Enhancements
- Budgeting features
- Recurring transactions
- User profile settings
- Mobile-friendly design
- Advanced machine learning expense predictions

