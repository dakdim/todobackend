from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskGetCreate(generics.ListCreateAPIView):
       queryset =Task.objects.all()
       serializer_class =TaskSerializer

class TaskUpdateDelete(generics.RetrieveUpdateDestroyAPIView):    
       queryset=Task.objects.all()
       serializer_class =TaskSerializer

