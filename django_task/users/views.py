from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer


class ProfileAPIView(RetrieveUpdateAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializer

    def get_object(self):
        user = self.request.user
        profile = get_object_or_404(Profile.objects.filter(user=user))
        return profile
