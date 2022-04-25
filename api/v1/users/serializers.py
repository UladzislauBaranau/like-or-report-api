from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers, validators

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(
                queryset=Profile.objects.all(),
                message="This email already exists.",
            ),
        ],
        allow_blank=False,
    )

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "password",
        ]

    def save(self):
        # Save the provided password in hashed format.
        user = super().save()
        user.set_password(user.password)
        user.save()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims.
        token["username"] = user.username
        if user.first_name and user.last_name:
            token["first_name"] = user.first_name
            token["last_name"] = user.last_name

        return token


class UpdateUserProfileSerializer(RegisterSerializer, serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()

        return instance


class ChangeUserPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(allow_blank=False)
    new_password = serializers.CharField(
        validators=[validate_password],
        allow_blank=False,
    )
