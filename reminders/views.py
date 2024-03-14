from django.shortcuts import render
from rest_framework import generics
from.serializers import ReminderSerializers

# Create your views here.

class CreateReminderView(generics.CreateAPIView):
    serializer_class= ReminderSerializers