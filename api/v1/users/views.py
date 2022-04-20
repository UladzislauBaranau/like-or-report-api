from api.v1.users.serializers import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework import mixins, permissions, viewsets

from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    """
    Takes a extra set of user credentials and
    returns customizing JSON web token.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
