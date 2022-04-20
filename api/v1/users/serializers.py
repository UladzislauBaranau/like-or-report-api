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
