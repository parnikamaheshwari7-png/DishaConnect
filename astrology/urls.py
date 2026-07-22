from django.urls import path
from . import views

urlpatterns=[
    path("", views.astrology_home, name='astrology_home'),
     path(
        'generate-kundali/',
        views.generate_kundali,
        name='generate_kundali'
    ),

    path(
        'kundali/<int:chart_id>/',
        views.kundali_result,
        name='kundali_result'
    ),

    path(
    'panchang/',
    views.today_panchang,
    name='today_panchang'
),

path(
    'kundali-matching/',
    views.kundali_matching,
    name='kundali_matching'
),
]