from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            name=validated_data['name'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    name_field = User.USERNAME_FIELD

    def validate(self, attrs):
        authenticate_kwargs = {
            self.name_field: attrs.get(self.name_field),
            "password": attrs.get("password"),
        }

        user = authenticate(**authenticate_kwargs)

        if not user:
            raise serializers.ValidationError("Неверное имя или пароль")

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            },
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["name"] = user.name
        return token

#  Добавляем сериализатор профиля
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'bio', 'avatar']
