from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import string
import random


def gen_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=32, unique=True, default=gen_code)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.short_code


class Visit(models.Model):
    short = models.ForeignKey(ShortURL, on_delete=models.CASCADE, related_name='visits')
    ip = models.CharField(max_length=64, blank=True)
    user_agent = models.CharField(max_length=256, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
