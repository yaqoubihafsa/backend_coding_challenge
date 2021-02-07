from rest_framework import serializers
from .models import Repository


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository # this is the model that is being serialized
        fields = ('name', 'language', 'url')