from api.v1.users.permissions import IsProfileOwner
from api.v1.users.serializers import (
    ChangeUserPasswordSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UpdateUserProfileSerializer,
)

from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response

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


class ChangeUserPasswordView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    The profile owner can change password.
    """

    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsProfileOwner)
    serializer_class = ChangeUserPasswordSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password.
            if not instance.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Set a new password.
            instance.set_password(serializer.data.get("new_password"))
            instance.save()
            response = {
                "status_code": status.HTTP_200_OK,
                "message": "Password updated successfully",
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
