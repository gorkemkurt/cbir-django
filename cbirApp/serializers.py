from rest_framework import serializers

from cbirApp.models import Images


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['name']
