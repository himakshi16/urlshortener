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
<img width="1817" height="912" alt="image" src="https://github.com/user-attachments/assets/5e71d053-2160-457e-a179-19bd28f2be15" />

<img width="1326" height="615" alt="image" src="https://github.com/user-attachments/assets/efe7c787-7983-4dc6-9b5b-4b9b10333e37" />

<img width="1315" height="912" alt="image" src="https://github.com/user-attachments/assets/9750b07a-2e31-48aa-9e12-20d98b5cbfb4" />
