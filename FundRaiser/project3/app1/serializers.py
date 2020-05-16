from app1.models import Donate, OrganizationName
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class DonateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user = UserSerializer()
        model = Donate
        fields = '__all__'

class OrganizationNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrganizationName
        fields = '__all__'