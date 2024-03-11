from django.urls import path
from warehouse import views


urlpatterns = [
    path("api/", views.OrderProductView.as_view()),
]