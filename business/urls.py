from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.UserListView.as_view()),
    path('users/<int:id>/', views.UserDetailView.as_view()),
    path('create/',views.UserCreateView.as_view()),
    path('directions/', views.GeektechDirectionsView.as_view()),

]