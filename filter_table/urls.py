from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MetadataHTMxTableView2.as_view(), name='table'),
    path('add-study/<str:acc_id>', views.add_study, name='add_study'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)