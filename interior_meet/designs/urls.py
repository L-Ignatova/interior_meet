from django.urls import path

from interior_meet.designs.views import add_page

urlpatterns = [
    path('add/', add_page, name='add'),
]