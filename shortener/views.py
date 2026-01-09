from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ShortURL, Visit
from django.contrib.auth.decorators import login_required
import qrcode
from io import BytesIO
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.urls import reverse
from base64 import b64encode
import json


def index(request):
    # If a production frontend build exists, serve its index.html (SPA)
    from pathlib import Path
    dist_index = Path(__file__).resolve().parent.parent / 'frontend' / 'dist' / 'index.html'
    if dist_index.exists():
        return HttpResponse(dist_index.read_text(encoding='utf-8'), content_type='text/html')
    return HttpResponse('Frontend not built yet. Run: cd frontend && npm run build')




# Removed: shorten() and detail() views (replaced by JSON API endpoints)


def redirect_short(request, code):
    try:
        obj = ShortURL.objects.get(short_code=code)
    except ShortURL.DoesNotExist:
        return HttpResponseNotFound('Short code not found')
    Visit.objects.create(short=obj, ip=request.META.get('REMOTE_ADDR',''), user_agent=request.META.get('HTTP_USER_AGENT',''))
    return redirect(obj.original_url)


def qr_code(request, code):
    obj = get_object_or_404(ShortURL, short_code=code)
    url = request.build_absolute_uri(f"/s/{obj.short_code}/")
    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf, format='PNG')
    return HttpResponse(buf.getvalue(), content_type='image/png')


@login_required

# Removed: analytics() and generate_qr() views (replaced by JSON API endpoints)@csrf_exempt
def api_generate_qr(request):
    # Accept JSON body or form-encoded
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    url = request.POST.get('qr_url') or (json.loads(request.body.decode('utf-8')).get('qr_url') if request.body else None)
    if not url:
        return JsonResponse({'error': 'qr_url required'}, status=400)
    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf, format='PNG')
    data = b64encode(buf.getvalue()).decode('ascii')
    return JsonResponse({'qr_data': data, 'url': url})


@csrf_exempt
def api_shorten(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)
    body = None
    try:
        body = json.loads(request.body.decode('utf-8')) if request.body else {}
    except Exception:
        body = {}
    original = request.POST.get('original_url') or body.get('original_url')
    if not original:
        return JsonResponse({'error': 'original_url required'}, status=400)
    obj = ShortURL.objects.create(original_url=original)
    short_url = request.build_absolute_uri(f"/s/{obj.short_code}/")
    # build QR as base64
    img = qrcode.make(short_url)
    buf = BytesIO()
    img.save(buf, format='PNG')
    data = b64encode(buf.getvalue()).decode('ascii')
    return JsonResponse({'short_code': obj.short_code, 'short_url': short_url, 'qr_data': data})


def api_recent(request):
    recent = ShortURL.objects.order_by('-created_at')[:20]
    items = [{'original_url': s.original_url, 'short_code': s.short_code, 'short_url': request.build_absolute_uri(f"/s/{s.short_code}/")} for s in recent]
    return JsonResponse({'recent': items})
