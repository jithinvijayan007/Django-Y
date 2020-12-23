from rest_framework import serializers
from cust_app.models import Customer, Services, SalesData

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class SalesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesData
        fields = "__all__"
