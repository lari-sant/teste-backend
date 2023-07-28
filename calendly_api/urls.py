from django.urls import path
from calendly_app import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('connect-google-calendar/', views.connect_google_calendar, name='connect_google_calendar'),
    path('set-available-schedule/', views.set_available_schedule, name='set_available_schedule'),
    path('get-available-schedules/<int:user_id>/', views.get_available_schedules, name='get_available_schedules'),
    path('schedule-event/<int:user_id>/', views.schedule_event, name='schedule_event'),
]
