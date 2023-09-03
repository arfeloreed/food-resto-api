from django.urls import path

from . import views

# urls below
urlpatterns = [
    path("", views.index, name="home"),
    path("<int:pk>/", views.food_detail, name="food-detail"),
]
