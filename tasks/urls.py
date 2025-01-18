from django.urls import path,include
from .views import TaskGetCreate,TaskUpdateDelete

urlpatterns = [
    path('',TaskGetCreate.as_view()),
    path('<int:pk>',TaskUpdateDelete.as_view()),
]

