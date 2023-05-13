from django.urls import path
from .views import HomePageview
	
urlpatterns =[
    path("", HomePageview.as_view(), name="home",)
]
