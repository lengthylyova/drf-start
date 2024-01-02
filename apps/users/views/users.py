from ..models import User
from ..permissions import IsUserOrReadOnly
from ..serializers.user import UserSerializer, CreateUserSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny



class UserViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    '''
        Updates and retrieves user accounts
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)



class UserCreateViewSet(CreateModelMixin, GenericViewSet):
    '''
        Creates user accounts
    '''
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
