from django.urls import path
from . import views

urlpatterns = [
    path("recommend-loans/", views.recommend_loans_view),
    path("recommend-properties/", views.recommend_properties_view),
]
