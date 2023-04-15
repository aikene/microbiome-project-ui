from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.filter_table, name='filter_table'),
    path('table/', views.MetadataHTMxTableView.as_view(), name='table'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)