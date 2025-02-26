from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers1 import delocationse
from rest_framework import status,filters
from django.views.decorators.cache import cache_page
'''
My name is Abdallah shref
UI/UX Designer
Backend Developer
I Use Django(DRF) in this project
'''
@cache_page(60*15)
@api_view(['GET','POST'])
def Ivison(request):
    '''
    this is get request and post request
    '''
    if request.method == 'GET':
        data = delocation.objects.all().order_by('pk')
        serializer = delocationse(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = delocationse(data=request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@cache_page(60*60)  # Cache the response for 1 hour
@api_view(['GET','PUT','DELETE','PATCH'])
def RestIvison(request,pk):
    try:
        data = delocation.objects.get(pk=pk)
    except delocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = delocation.objects.get(pk=pk)
        serializer = delocationse(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = delocationse(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = delocationse(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
