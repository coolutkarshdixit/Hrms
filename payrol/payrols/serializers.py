from rest_framework import serializers
from .models import Payroluser


class PayrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroluser
        fields = '__all__'
