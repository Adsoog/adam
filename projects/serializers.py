from rest_framework import serializers
from .models import Project, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('client_name',)

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Project
        fields = ('client', 'sap_code', 'ov_name')