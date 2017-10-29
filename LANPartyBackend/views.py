# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from models import Inscripcions, Tiquets
from serializers import InscripcioSerializer, TiquetSerializer

@csrf_exempt
def inscripcio_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Inscripcions.objects.all()
        serializer = InscripcioSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def inscripcio_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Inscripcions.objects.get(pk=pk)
    except Inscripcions.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InscripcioSerializer(snippet)
        return JsonResponse(serializer.data)

@csrf_exempt
def tiquets_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Tiquets.objects.all()
        serializer = TiquetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TiquetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class tiquet_by_qr(generics.ListAPIView):
    serializer_class = TiquetSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        qr = self.kwargs['qr_id']
        return Tiquets.objects.filter(qr_id=qr)
