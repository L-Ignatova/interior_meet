from django.urls import path

from interior_meet.designs.views import landing_page, add_page

urlpatterns = [
    path('add/', add_page, name='add'),
]