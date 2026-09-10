from django.core.mail import send_mail
from django.http import HttpResponse


def send_test_email(request):
    subject = 'Welcome to my blog'
    message = 'Thank you for subscribing to my blog!'
    from_email = 'your_email@gmail.com'
    recipient_list = ['shubham1@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse("Test email sent successfully")