from django.urls import path

from interior_meet.designs.views import list_designs, create_design

urlpatterns = [
    path('', list_designs, name='all designs'),
    path('create/', create_design, name='create design'),
]