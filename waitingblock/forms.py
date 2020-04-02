from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.forms import ModelForm
from .models import Customer, News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
#       self.helper.form_id = 'customerform-id'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add'))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'name',
            'partysize',
            'contact',
#            'status',
        )

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
#       self.helper.form_id = 'customerform-id'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add'))


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('status', )

#    def update_db_field(customer, status, value):
#        Customer.objects.get(name=name).update(field=True)
#    status = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Seat'))

#        self.helper.form_method = 'post'
#        self.helper.add_input(Submit('submit', 'Save person'))
