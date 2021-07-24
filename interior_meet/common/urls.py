from django.urls import path

from interior_meet.designs.views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),

]