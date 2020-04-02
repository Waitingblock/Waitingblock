#models
import uuid
import django_tables2 as tables
import datetime

from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.utils.timesince import timesince
from django.utils.timezone import utc
from phonenumber_field.modelfields import PhoneNumberField

#from django.contrib.auth.models import AbstractUser

#from django_tables2 import MultiTableMixin
#from django.forms import ModelForm


BOOL_CHOICES = ((True, 'Waiting'), (False, 'Seated'))

class News(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=2048, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)


class Restaurant(models.Model):
    Restaurant_name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    contact = PhoneNumberField(blank=True)
    slug = models.SlugField()
    location = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    #    features = models.ManyToManyField() # dinner, launch, nightlife,
    #    timing = models.ManyToManyField() # sunday, monday, tuesday,
    delivery = models.BooleanField(default=False)


#    image = models.ImageField()


class Customer(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
#    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    partysize = models.IntegerField()
    arrival_time = models.DateTimeField(auto_now_add=True, blank=True)
    contact = PhoneNumberField(blank=True)
    status = models.BooleanField(choices=BOOL_CHOICES, default=True)

    def get_time_diff(self):
        if self.arrival_time:
            now = datetime.datetime.utcnow().replace(tzinfo=utc)
            timediff = now - self.arrival_time
            return timediff.total_seconds()

    wait = get_time_diff

    def __str__(self):
        return self.name

        class Meta:
            verbose_name = 'Customer'
            verbose_name_plural = 'Customers'
            ordering = ['-arrival_time']


# class SoftDeleteModel(News):
#   class meta:
#       abstract = True
      
#   is_deleted = models.DateTimeField(null=False, default=False)

#   def delete(self):
#     self.is_deleted = True
#     self.save()

#   def restore(self):
#     self.is_deleted = False
#     self.save()

