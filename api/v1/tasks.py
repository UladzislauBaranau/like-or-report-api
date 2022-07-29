from celery import shared_task

from django.core.mail import send_mail


@shared_task()
def send_greeting(username, email):
    send_mail(
        "You have successfully registered",
        f"Welcome {username}!",
        None,
        [email],
        fail_silently=False,
    )
