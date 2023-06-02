from rest_framework.views import APIView
from rest_framework.response import Response
from admin1.models import Sample,TeamLeaderData
from admin1.serializers import SampleSerializer,TeamLeaderDataSerializer

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


