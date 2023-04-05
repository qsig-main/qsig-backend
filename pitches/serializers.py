from rest_framework import serializers
from .models import Pitch, PitchImage
from api.serializers import UserPublicSerializer
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

class PitchSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='pitch-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Pitch
        fields = [
            'title',
            'pdf',
            'do_not_display',
            'order',
            'pk',
            'url',
            'date_created',
            'cover',
        ]



class PitchImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PitchImage
        fields = [
            'title',
            'image',
            'do_not_display',
            'order',
            'pk',
            'date_created',
        ]