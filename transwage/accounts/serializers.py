from rest_framework import serializers
from . import models


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Job
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Contract
        fields = "__all__"
