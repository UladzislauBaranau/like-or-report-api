from rest_framework import serializers, validators

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
