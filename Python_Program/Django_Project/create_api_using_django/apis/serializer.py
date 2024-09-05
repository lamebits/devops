from rest_framework import serializers
from .models import ApiModel

class APISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiModel
        fields = ('title','description')