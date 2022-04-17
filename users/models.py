from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    is_blocked = models.BooleanField(
        default=False,
        help_text="Designates that this user has blocked.",
    )

    def __str__(self):
        return f"{self.username}, blocked: {self.is_blocked}"

    class Meta:
        ordering = ("id",)
