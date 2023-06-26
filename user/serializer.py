from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Users.objects.all())])
    username = serializers.CharField(min_length=4, validators=[UniqueValidator(queryset=Users.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = ['username', 'password', 'email']
        extra_kwargs = {"password": {'write_only': True}}


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300)
    password = serializers.CharField()

    class Meta:
        model = Users
        fields = ["token"]


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail("Invalid token")
