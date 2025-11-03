import django_filters
from .models import Employee
class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact') ## to handle case insensitive filtering
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains') ## to handle partial matching and case insensitive filtering
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range',label='from ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='to ID')



    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        
        return queryset

    class Meta:
        model = Employee
        fields = ['designation','emp_name','id_min','id_max']