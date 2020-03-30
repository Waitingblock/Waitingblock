from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls import url
from django.urls import include, path
from waitingblock.views import WaitingblockView, CustomerUpdateView, TablesView, newslist, delete
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', WaitingblockView.as_view(), name='home'),
    path('newslist/', views.newslist, name='newslist'),
    path('delete/<uid>', views.delete, name='delete'),
    path('success/', WaitingblockView.redirect_view),
    path('update/', CustomerUpdateView.as_view(), name='status_update'),
    path('tables/', TablesView.as_view(), name='tables'),
    path('registration/', include('django.contrib.auth.urls')),
    path('registration/signup/', views.SignUp.as_view(), name='signup'),
]
