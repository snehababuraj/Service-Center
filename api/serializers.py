from rest_framework import serializers

from api.models import Customer,Work

class WorkSerializer(serializers.ModelSerializer):

    customer=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Work

        fields="__all__"

        read_only_fields=["id","created_date","update_date","is_active","customer"]

class CustomerSerializer(serializers.ModelSerializer):

    technician=serializers.StringRelatedField(read_only=True)

    works=WorkSerializer(many=True,read_only=True)

    work_count=serializers.CharField(read_only=True)

    work_total=serializers.CharField(read_only=True)

    class Meta:

        model=Customer

        fields="__all__"

        read_only_fields=["id","technician","created_date","update_date","is_active","status"]