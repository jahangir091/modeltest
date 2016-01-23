from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View
from models import Person
from rest_framework import serializers


class TestView(View):
    def get(self, request):
        d = Person.objects.get(id=1)


        return HttpResponse(d.first_name)


