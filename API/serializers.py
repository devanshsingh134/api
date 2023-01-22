from rest_framework import serializers
from crud.models import Member



class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=['id','firstname', 'lastname']