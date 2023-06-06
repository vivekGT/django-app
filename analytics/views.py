from rest_framework.views import APIView
from rest_framework.response import Response
from admin1.models import Sample,TeamLeaderData,User,salesEx
from admin1.serializers import SampleSerializer,TeamLeaderDataSerializer,userSerializer,salesExSerializer

class DataAnalyticsAPIView(APIView):
    def get(self, request):
        data = Sample.objects.all()
        serializer = SampleSerializer(data, many=True)
        return Response(serializer.data)
class DataAnalytics2APIView(APIView)   :
    def get(self,request):
        data=TeamLeaderData.objects.all()
        searializer=TeamLeaderDataSerializer(data,many=True)
        return Response(searializer.data)
    
from rest_framework import generics


class userAPIView(APIView):
    def get(self, request):     
        data =User.objects.all()
        serializer=userSerializer(data,many=True)
        return Response(serializer.data)

class salesExAPIView(APIView):
    def get(self,request):
        data=salesEx.objects.all()
        serializer=salesExSerializer(data,many=True)
        return Response(serializer.data)

