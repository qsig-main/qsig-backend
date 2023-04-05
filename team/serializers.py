from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='pitch-detail',
        lookup_field='pk'
    )
    
    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'position',
            'headshot',
            'year',
            'vertical',
            'custom_vertical',
            'company',
            'LinkedIn',
            'do_not_display',
            'order',
            'url',
        ]

    # extra_kwargs = {'display': {'default': True}}
