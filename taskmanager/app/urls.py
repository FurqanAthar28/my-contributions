from django.urls import path
from .views import  *
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('task/',TaskListCreateView.as_view(), name='task'),
    path('task/<int:pk>/',TaskDetailView.as_view(), name='task-detail'),
]