from django.core.validators import RegexValidator
from companies.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ['creation_date', 'update_date']


