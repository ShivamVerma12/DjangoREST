from .views import StudentView
from django.urls import path

urlpatterns = [
    path('basic/', StudentView.as_view()),
    path('update/<int:pk>/', StudentView.as_view()),

]
