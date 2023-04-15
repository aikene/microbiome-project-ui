import django_filters
import django_tables2 as tables
from django.db import models
from app.models import Metadata


class SRAMetadataTable(tables.Table):
    selection = tables.CheckBoxColumn()

    class Meta:
        model = Metadata
        template_name = "templates/bootstrap_htmx.html"


class MetadataFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Metadata
        fields = ['query']