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
   

# ****************************************************************************************************************************
'''
the  following commented code also work same as above...

'''
# from django.shortcuts import render
# from .serializers import MemberSeriializer
# from crud.models import Member
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
#
#
#
# # Create your views here.
#
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def MemberAPI(request, pk):
#     if request.method=='GET':
#
#
#         if id is not None:
#             stu = Member.objects.get(pk=pk)
#             serializer = MemberSerializer(stu)
#             return Response(serializer)
#     stu = Member.objects.all()
#     serializer = MemberSerializer(stu, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type="application/json")
#
# def post(self, request, *args, **kwargs):
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     serializer = MemberSerializer(data=pythondata)
#     if serializer.is_valid():
#         serializer.save()
#         res = {'msg': 'data saved'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type="application/json")
#
# def put(self, request, *args, **kwargs):
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     id = pythondata.get('id')
#     stud = Member.objects.get(id=id)
#     serializer = MemberSerializer(stud, data=pythondata, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         res = {'msg': "updated"}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type='application/json')
#
# def delete(self, request, *args, **kwargs):
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     id = pythondata.get('id')
#     stud = Member.objects.get(id=id)
#     stud.delete()
#     res = {"msg": "deleted"}
#     json_data = JSONRenderer().render(res)
#     return HttpResponse(json_data, content_type='application/json')



