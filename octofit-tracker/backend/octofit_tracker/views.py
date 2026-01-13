from rest_framework import viewsets
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from octofit_tracker.serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    WorkoutSerializer, LeaderboardSerializer
)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
