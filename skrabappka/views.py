from django.shortcuts import render
from rest_framework.views import APIView
from .models import Scratching
from .serializers import ScratchingSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.
def index(request):
    scratchings = Scratching.objects.filter(date=datetime.today()).order_by('dateandtime')
    return render(request, 'skrabappka.html', {'scratchings': scratchings})

def summary(request):
    bucanek = Scratching.objects.filter(person='Bucanek').aggregate(Sum('minutes'))['minutes__sum']
    bulva = Scratching.objects.filter(person='Bulva').aggregate(Sum('minutes'))['minutes__sum']
    return JsonResponse({'bucanek': bucanek, 'bulva': bulva}, safe=True)


class ScratchingList(APIView):
    def get(self, request, format=None):
        observations = Scratching.objects.filter(date=datetime.today()).order_by('dateandtime')
        serializer = ScratchingSerializer(observations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScratchingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
