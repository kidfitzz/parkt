from django.contrib import admin
from django.urls import path, include
from course_keeper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course_keeper.urls'))
]
