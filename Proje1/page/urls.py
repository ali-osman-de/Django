from django.urls import path
from page.views import (
    home_view, 
    about_us_view,
    contact_us_view)


urlpatterns = [
    path('', home_view, name="home"),
    path('aboutus/', about_us_view, name="aboutus"),
    path('contact/', contact_us_view, name="contactus"),
]