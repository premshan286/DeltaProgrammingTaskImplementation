from django.contrib import admin
from django.urls import include, path
from api import views
from django.conf.urls import url

urlpatterns = [

	#Paths for the REST API calls
	path('origin-api/', views.origin_api),
	path('destination-api/', views.destination_api),
	path('search-api/', views.search_api),

	#Path for the search from UI
	path('flightSearch/', views.flightSearch, name='flightSearch'),

]
