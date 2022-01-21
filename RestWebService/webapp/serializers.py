from rest_framework import serializers
from webapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields=('firstname','lastname','emp_id')
        fields = "__all__"
