from django.urls import path

from webapp.views import index, cat_status

urlpatterns = [
    path('', index),
    path('cat_status/', cat_status),
]
