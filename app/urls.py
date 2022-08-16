from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.client.urls")),
    path("api/auth/", include("app.telegram_auth.urls")),
]
