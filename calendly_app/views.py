
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import CustomUser, AvailableSchedule, ScheduledEvent, GoogleCalendarConnection
from .serializers import (
    CustomUserSerializer,
    GoogleCalendarConnectionSerializer,
    AvailableScheduleSerializer,
    ScheduledEventSerializer,
)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    # Implement your user login logic here and return an appropriate response


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def connect_google_calendar(request):
    user = request.user
    try:
        existing_connection = GoogleCalendarConnection.objects.get(user=user)
        serializer = GoogleCalendarConnectionSerializer(existing_connection, data=request.data)
    except GoogleCalendarConnection.DoesNotExist:
        serializer = GoogleCalendarConnectionSerializer(data=request.data, context={'user': user})
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_available_schedule(request):
    serializer = AvailableScheduleSerializer(data=request.data, context={'user': request.user})
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_available_schedules(request, user_id):
    try:
        user = CustomUser.objects.get(pk=user_id)
        schedules = AvailableSchedule.objects.filter(user=user)
        serializer = AvailableScheduleSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CustomUser.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([AllowAny])
def schedule_event(request, user_id):
    # Implement logic to schedule an event with a specific user and return an appropriate response
