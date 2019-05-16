from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('dash/', dash, name="dash"),
    path('dashboardgr/', dashboardgr, name="dashboardgr"),
    path('test/', test, name ="test"),
    path('table/', table, name="table"),
    path('ajax/', add_ajax, name="add_ajax"),
    path('ajaxtwo/', add_ajaxtwo, name="add_ajaxtwo"),
    path('ajaxthree/', add_ajaxthree, name="add_ajaxthree"),
    path('display_data/', display_data, name="display_data"),

    path('fridge/', fridge, name="fridge"),
    path('redshelf/', redshelf, name="redshelf"),
    path('panorama/', panorama, name="panorama"),

]
