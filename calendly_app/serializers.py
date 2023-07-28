
from rest_framework import serializers
from .models import CustomUser, AvailableSchedule, ScheduledEvent


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_active']


class GoogleCalendarConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleCalendarConnection
        fields = '__all__'


class AvailableScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableSchedule
        fields = ['id', 'date_time']


class ScheduledEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEvent
        fields = '__all__'
