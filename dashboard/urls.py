# dashboard/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define your homepage view here
    path('contact/', views.contact, name='contact'),  # Contact page
    path('reporting/', views.reporting_form, name='reporting_form'),  # Reporting form page
    path('submit_report/', views.submit_report, name='submit_report'),  # Handle report submission
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard view
]
