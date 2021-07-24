from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interior_meet.common.urls')),
    path('designs/', include('interior_meet.designs.urls')),
]
