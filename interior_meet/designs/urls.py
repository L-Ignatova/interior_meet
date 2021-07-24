from django.urls import path

from interior_meet.designs.views import add_page, list_designs

urlpatterns = [
    path('', list_designs, name='all designs'),
    path('add/', add_page, name='add'),
]