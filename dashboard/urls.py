from django.urls import path
from . import views

urlpatterns=[
    path("profile/", views.my_profile, name="profile"),
     path(
        "guide/",
        views.guide_dashboard,
        name="guide_dashboard"
    ),
]