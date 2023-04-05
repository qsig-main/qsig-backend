from django.shortcuts import render
from rest_framework import generics
from .models import Report, ReportImage
from .serializers import ReportSerializer, ReportImageSerializer

class ReportListAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
report_list_view = ReportListAPIView.as_view()

class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save()
report_create_view = ReportCreateAPIView.as_view()


class ReportDetailAPIView(generics.RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
report_detail_view = ReportDetailAPIView.as_view()


class ReportUpdateAPIView(generics.UpdateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

report_update_view = ReportUpdateAPIView.as_view()


class ReportDestroyAPIView(generics.DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

report_destroy_view = ReportDestroyAPIView.as_view()


class ReportImageListAPIView(generics.ListAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer
report_image_list_view = ReportImageListAPIView.as_view()

class ReportImageCreateAPIView(generics.CreateAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer

    def perform_create(self, serializer):
        serializer.save()
report_image_create_view = ReportImageCreateAPIView.as_view()


class ReportImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer
report_image_detail_view = ReportImageDetailAPIView.as_view()


class ReportImageUpdateAPIView(generics.UpdateAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

report_image_update_view = ReportImageUpdateAPIView.as_view()


class ReportImageDestroyAPIView(generics.DestroyAPIView):
    queryset = ReportImage.objects.all()
    serializer_class = ReportImageSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

report_image_destroy_view = ReportImageDestroyAPIView.as_view()