from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from .models import Member
from .serializers import MemberSerializer


class MemberListAPIView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
member_list_view = MemberListAPIView.as_view()

class MemberDetailAPIView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
member_detail_view = MemberDetailAPIView.as_view()

class MemberCreateAPIView(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.save()
member_create_view = MemberCreateAPIView.as_view()

class MemberUpdateAPIView(generics.UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
member_update_view = MemberUpdateAPIView.as_view()

class MemberDestroyAPIView(generics.DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
member_destroy_view = MemberDestroyAPIView.as_view()