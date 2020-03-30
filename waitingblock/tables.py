#tables

import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from .models import Customer, News


# class CustomerTable(tables.Table):
#     name = tables.Column()
#     wait = tables.Column(order_by=('arrival_time'))
#     partysize = tables.Column()
#     arrival_time = tables.Column()
#     status = tables.Column()
#     contact = tables.Column()
#     seat = tables.LinkColumn('status_update', accessor='pk', text='✔️')

#     class Meta:
#         data = Customer.objects.all()


# class CustomerUpdateTable(tables.Table):
#     name = tables.Column()
#     wait = tables.Column(order_by=('arrival_time'))
#     partysize = tables.Column()
#     arrival_time = tables.Column()
#     status = tables.Column()
#     contact = tables.Column()

#     class Meta:
#         data = Customer.objects.all()

class MaterializeCssCheckboxColumn(tables.CheckBoxColumn):
    def render(self, value, bound_column, record):
        default = {"type": "checkbox", "name": bound_column.name, "value": value}
        if self.is_checked(value, record):
            default.update({"checked": "checked"})

        general = self.attrs.get("input")
        specific = self.attrs.get("td__input")
        attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
        return mark_safe("<p><label><input %s/><span></span></label></p>" % attrs.as_html())

class NewsTable(tables.Table):
    created = tables.DateTimeColumn(format='m/d H\h\s')
    check = MaterializeCssCheckboxColumn(accessor='uid')

    class Meta:
        model = News
        fields = ('check', 'title', 'created', 'modified', 'status', 'is_deleted')
