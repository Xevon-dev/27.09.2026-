from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arithmetic_sum/' , views.arithmetic_sum ),
    path("result/", views.result),
    path("feedback/", views.feedback),
    path("rating/", views.rating)
]
