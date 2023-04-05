from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from pitches.serializers import PitchSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    serializer = PitchSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "bad data"}, status=400)

