from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from src.users.models import User
from src.users.serializers import CreateUserSerializer, UserSerializer


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates user accounts
    """

    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
