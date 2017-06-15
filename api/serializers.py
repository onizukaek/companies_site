from django.contrib.auth.models import User
from companies.models import Company
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    companies = serializers.PrimaryKeyRelatedField(many=True, queryset=Company.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'companies')


class CompanySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Company
        fields = '__all__'
