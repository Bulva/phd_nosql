from rest_framework import serializers
from .models import Scratching


class ScratchingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scratching
        fields = ('id', 'dateandtime', 'date', 'person', 'minutes')