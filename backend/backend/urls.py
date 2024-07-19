from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', views.get_data),
    path('api/create/', views.create_item),
]
