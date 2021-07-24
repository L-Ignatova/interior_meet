from django.urls import path

from interior_meet.designs.views import list_designs, create_design, design_details, edit_design

urlpatterns = [
    path('', list_designs, name='all designs'),
    path('details/<int:pk>', design_details, name='design details'),
    path('create/', create_design, name='create design'),
    path('edit/<int:pk>', edit_design, name='edit design'),
]