from django.shortcuts import render
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from filter_table.tables import SRAMetadataTable, MetadataFilter
from app.models import Metadata


# Create your views here.
def filter_table(request):
    columns = ['col1', 'col2']

    return render(request, 'filtered_table.html', {
        "data": columns
    })


class MetadataHTMxTableView(SingleTableMixin, FilterView):
    table_class = SRAMetadataTable
    queryset = Metadata.objects.all()
    filterset_class = MetadataFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "product_table_htmx.html"

        return template_name
