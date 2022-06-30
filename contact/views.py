from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactSerializer
from .models import Contact


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()