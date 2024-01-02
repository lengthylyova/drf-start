from ..models import User
from rest_framework.serializers import ModelSerializer



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email',
            'first_name', 'last_name',
        ]
        read_only_fields = ('email', )
        


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email', 'password',
            'first_name', 'last_name',
        ]
        extra_kwargs = {'password': {'write_only': True}}