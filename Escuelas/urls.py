from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="Home"),
	path("detalles/<str:id>/", view=views.Detalles, name="Detalles"),
]
