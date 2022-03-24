from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('himaldarshanadmin/', admin.site.urls),
    path('', include('student.urls')),
]
