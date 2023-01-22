from crud.models import Member
from rest_framework import viewsets
from .serializers import MemberSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class= MemberSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

