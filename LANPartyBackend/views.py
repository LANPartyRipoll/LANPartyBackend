# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Inscripcions, Tiquets
from .serializers import InscripcioSerializer, TiquetSerializer

@csrf_exempt
def inscripcio_detail(request, qr):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tiquet = Tiquets.objects.get(qr_id=qr)
        inscripcio = tiquet.inscripcio
    except Tiquets.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InscripcioSerializer(inscripcio)
        return JsonResponse(serializer.data)
