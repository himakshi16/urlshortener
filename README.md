# URL Shortener & QR Code Generator

A Django app to shorten URLs, generate QR codes, track visits and show simple expense graphs.

Quick start

1. Create and activate a virtualenv (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations and start server:

```powershell
python manage.py migrate
python manage.py runserver
```

3. Visit `http://127.0.0.1:8000/` to use the app.

Notes

- Uses SQLite by default.
- QR codes require `qrcode` and `Pillow`.
