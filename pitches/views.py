from django.shortcuts import render
from rest_framework import generics
from .models import Pitch, PitchImage
from .serializers import PitchSerializer, PitchImageSerializer #, PitchCreateSerializer
import os

class PitchListAPIView(generics.ListAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer
pitch_list_view = PitchListAPIView.as_view()

class PitchCreateAPIView(generics.CreateAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer

    def perform_create(self, serializer):
        serializer.save()
pitch_create_view = PitchCreateAPIView.as_view()


class PitchDetailAPIView(generics.RetrieveAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer
pitch_detail_view = PitchDetailAPIView.as_view()


class PitchUpdateAPIView(generics.UpdateAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

pitch_update_view = PitchUpdateAPIView.as_view()


class PitchDestroyAPIView(generics.DestroyAPIView):
    queryset = Pitch.objects.all()
    serializer_class = PitchSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

pitch_destroy_view = PitchDestroyAPIView.as_view()


class PitchImageListAPIView(generics.ListAPIView):
    queryset = PitchImage.objects.all()
    serializer_class = PitchImageSerializer
pitch_image_list_view = PitchImageListAPIView.as_view()

class PitchImageCreateAPIView(generics.CreateAPIView):
    queryset = PitchImage.objects.all()
    serializer_class = PitchImageSerializer

    def perform_create(self, serializer):
        serializer.save()

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
pitch_image_create_view = PitchImageCreateAPIView.as_view()


class PitchImageDetailAPIView(generics.RetrieveAPIView):
    queryset = PitchImage.objects.all()
    serializer_class = PitchImageSerializer
pitch_image_detail_view = PitchImageDetailAPIView.as_view()


class PitchImageUpdateAPIView(generics.UpdateAPIView):
    queryset = PitchImage.objects.all()
    serializer_class = PitchImageSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

pitch_image_update_view = PitchImageUpdateAPIView.as_view()


class PitchImageDestroyAPIView(generics.DestroyAPIView):
    queryset = PitchImage.objects.all()
    serializer_class = PitchImageSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

pitch_image_destroy_view = PitchImageDestroyAPIView.as_view()