# test_db.py файл үүсгэх (төслийн үндсэн folder-т)
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms_project.settings')
django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"✅ MySQL холболт амжилттай!")
        print(f"MySQL верси: {version[0]}")
except Exception as e:
    print(f"❌ Алдаа гарлаа: {e}")