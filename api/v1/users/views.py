from api.v1.users.serializers import RegisterSerializer

from rest_framework import mixins, viewsets


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
