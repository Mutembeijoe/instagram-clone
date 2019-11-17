from django.urls import path
from .views import CreateUserView, DetailUserView


urlpatterns = [
    path('register/', CreateUserView.as_view(), name="register"),
    path('profile/<int:pk>/', DetailUserView.as_view(), name='profile')
]