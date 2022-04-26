from django.core.mail import send_mail
from django.dispatch import receiver

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(reset_password_token, *args, **kwargs):
    email_plaintext_message = f"token: {reset_password_token.key}"

    send_mail(
        # title:
        "Password Reset for Images website",
        # message:
        email_plaintext_message,
        # from:
        "images@somehost.local",
        # to:
        [reset_password_token.user.email],
    )
