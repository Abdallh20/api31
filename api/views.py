from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status,filters
# Create your views here.

@api_view(['GET','POST'])
def graduationproject(request):
    if request.method == 'GET':
        data = delocation.objects.all()
        serializer = locationSerializer(data,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = locationSerializer(data=request.data)
    if serializer.is_valid():   
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    # guest.objects.create(name=data['name'],emaiyl=data['email'],phone=data['phone'])
    return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE','PATCH'])
def graduationproject2(request,pk):
    try:
        data = delocation.objects.get(pk=pk)
    except delocation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = delocation.objects.get(pk=pk)
        serializer = locationSerializer(data)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = locationSerializer(data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = locationSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)