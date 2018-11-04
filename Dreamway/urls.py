"""Dreamway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import (
profile,
home,
register_page,
donor_page,
login_page,
user_logout,
contact_us,
about,
mission_vision,
organization,
available_donor,
last_donation_date,
photo_gallery,
# Blodd Type ****************************************
a_positive,
a_negative,
b_positive,
b_negative,
ab_positive,
ab_negative,
o_positive,
o_negative,

)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ****************** Accounts ********************
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register_page, name='register'),
    path('to-be-a-blood-donor/', donor_page, name='blood_donor_form'),
    path('login/', login_page, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', user_logout, name='logout'),
    path('contact-us/', contact_us, name='contact'),
    path('about/', about, name='about'),
    path('mission-vision/', mission_vision, name='mission_vision'),
    path('organization/', organization, name='organization'),
    path('blood-donors-information-2/', available_donor, name='available_donor'),
    path('your-last-donation-date/', last_donation_date, name='last_donation_date'),
    path('photo-gallery/', photo_gallery, name='photo_gallery'),
    # blood group *******************************************************************
    path('a-positive/', a_positive, name='a_positive'),
    path('a-negative/', a_negative, name='a_negative'),
    path('b-positive/', b_positive, name='b_positive'),
    path('b-negative/', b_negative, name='b_negative'),
    path('ab-positive/', ab_positive, name='ab_positive'),
    path('ab-negative/', ab_negative, name='ab_negative'),
    path('o-positive/', o_positive, name='o_positive'),
    path('o-negative/', o_negative, name='o_negative'),

]
