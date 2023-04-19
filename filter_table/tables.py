import django_filters
import django_tables2 as tables
from django.db import models
from app.models import Metadata
from django_tables2 import TemplateColumn



class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class SRAMetadataTable(tables.Table):
    selection = CheckBoxColumnWithName(accessor="acc", orderable=False, checked=True,
                                       verbose_name='Include in Visualization')
    add = TemplateColumn(template_name="add_study.html")

    class Meta:
        model = Metadata
        template_name = "./bootstrap_htmx.html"
        include = ('acc',)


class MetadataFilter(django_filters.FilterSet):
    search_query = django_filters.CharFilter(method='universal_search',
                                             label="")

    class Meta:
        model = Metadata
        fields = ['search_query']
