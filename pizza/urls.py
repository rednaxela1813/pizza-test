
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .views import coming_soon

print("=== ЗАГРУЗКА URLS.PY ===")  # 👈 Проверяем загрузку

def show_urls(request):
    return JsonResponse({"message": "Маршруты загружены!", "urls": ["admin/", "/"]})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", coming_soon),
    path("show-urls/", show_urls),
]
