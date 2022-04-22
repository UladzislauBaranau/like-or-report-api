from api.v1.users.permissions import IsProfileOwner
from api.v1.users.serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UpdateUserProfileSerializer,
)

from rest_framework import mixins, permissions, viewsets

from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Profile


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Takes a extra set of user credentials and
    returns customizing JSON web token.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UpdateUserProfileView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    The profile owner can update personal information.
    """

    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsProfileOwner)
    serializer_class = UpdateUserProfileSerializer
