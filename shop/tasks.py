import uuid
from datetime import timedelta

from celery import shared_task

from django.utils.timezone import now

from shop.models import Users, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = Users.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()
