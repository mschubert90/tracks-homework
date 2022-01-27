from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from API.models import *
from API.serializers import *


# Create your views here.
@csrf_exempt
def shipmentApi(request):
    start = request.GET.get('start', '2021-01-01')
    # add + "T23:59:59Z" to the end variable to have inclusive date ranges
    end = request.GET.get('end', '2021-12-31') + "T23:59:59Z"
    shipments = Shipments.objects.filter(dropoff_time__range=[start, end]).order_by("-dropoff_time")
    shipments_serializer = ShipmentsSerializer(shipments, many=True)
    return JsonResponse(shipments_serializer.data,safe=False)
