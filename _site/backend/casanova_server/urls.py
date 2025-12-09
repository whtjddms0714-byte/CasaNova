# backend/casanova_server/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("casanova_app.urls")),  # 추가
]
