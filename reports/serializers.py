from rest_framework import serializers
from .models import Report, ReportImage
from api.serializers import UserPublicSerializer


class ReportSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='report-detail',
        lookup_field='pk'
    )
    class Meta:
        model = Report
        fields = [
            # 'owner',
            # 'user',
            'title',
            # 'description',
            'pdf',
            'do_not_display',
            'order',
            'pk',
            'url',
            'date_created',
            'cover',
        ]

    
class ReportImageSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = ReportImage
        fields = [
            'title',
            'image',
            'do_not_display',
            'order',
            'pk',
            'date_created',
        ]