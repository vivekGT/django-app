from rest_framework import serializers
from .models import Sample,TeamLeaderData,salesEx
class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['Model', 'DMS_Stock', 'WS_TGT','WS_ACH','BAL_WS','Total_Probable_Stock']
class TeamLeaderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeamLeaderData
        fields=['team_leader_name','team_leader_territory','per_day_asking','enquiry_total','test_drive_percentage','home_visit_percentage']

from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class salesExSerializer(serializers.ModelSerializer):
    class Meta:
        model=salesEx
        fields='__all__'