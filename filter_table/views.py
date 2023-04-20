from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, LazyPaginator

from app.forms import MetadataForm
from app.models import Metadata
from filter_table.tables import SRAMetadataTable, MetadataFilter


# Create your views here.

class MetadataHTMxTableView2(SingleTableMixin, FilterView):
    all_fields = [field.name for field in Metadata._meta.get_fields()]

    table_class = SRAMetadataTable
    queryset = Metadata.objects.none()
    filterset_class = MetadataFilter
    # paginate_by = 15
    paginator_class = LazyPaginator

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "product_table_htmx.html"
        return template_name

    def get_table_kwargs(self):
        filter_dict = self.request.session.get('filter_dict', {})
        if filter_dict:
            exclude = set(self.all_fields) - set(filter_dict.keys())
        else:
            exclude = ('attributes',)
        return {
            'exclude': ('attributes', 'jattr',),
        }

    def get_table_data(self):
        filter_dict = self.request.session.get('filter_dict', {})
        query = Q()
        if filter_dict:
            for key, value in filter_dict.items():
                if isinstance(value, list):
                    query &= Q(**{f"{key}__in": value})
                else:
                    query &= Q(**{key: value})
            return Metadata.objects.filter(Q(query))
        else:
            queryset = self.queryset
        return queryset

    def post(self, request, *args, **kwargs):
        form = MetadataForm(request.POST)
        filter_dict = {}
        if form.is_valid():
            data = request.POST.dict()
            for key, value in data.items():
                if hasattr(Metadata, key):
                    filter_dict.update({key: value})

            request.session['filter_dict'] = filter_dict
        return self.get(request, *args, **kwargs)


def add_study(request, acc_id):
    print(acc_id)
    # table = MetadataHTMxTableView2(queryset=self.queryset)
    return JsonResponse({'acc': acc_id})
