from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Добро пожаловать',
        'Мы будем присылать вам QR код ',
        'kusov1.alex2004@mail.ru',
        [user_email],
        fail_silently=False)
