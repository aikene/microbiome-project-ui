from django_filters import Filter


class ListFilterField(Filter):

    def filter(self, queryset, value):

        # If no value is passed, just return the
        # initial queryset
        if not value:
            return queryset

        self.lookup_expr = 'iexact'  # Setting the lookupexpression for all values
        list_values = value.split(',')  # Split the incoming querystring by comma

        return super(ListFilterField, self).filter(queryset, list_values)