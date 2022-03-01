from django.core.mail import EmailMessage


def send_booking_update(user, booking):
    subject = f'[{booking.id}] {booking.service.name}'
    message = f'''
Hi {user.first_name},

Your booking has been updated.

<strong>State:</strong>      {booking.state}
<strong>Date:</strong>       {booking.date}
<strong>Comments:</strong>   {booking.mentions}

For questions, please contact us via email at'
'<strong>info@spotless.se</strong> or call us'
' at <strong>0754981234</strong>.'

Best regards,
Team Spotless
'''

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email='my.spotless.app@gmail.com',
        to=[user.email],
        reply_to=['my.spotless.app@gmail.com'],
    )
    mail.content_subtype = "html"
    mail.send()


def send_booking_cancelation(user, booking):
    subject = f'[{booking.id}] {booking.service.name}'
    message = f'''
Hi {user.first_name},

Your booking has been CANCELLED.

For questions, please contact us via email'
' at <strong>info@spotless.se</strong> or'
' call us at <strong>0754981234</strong>.'

Best regards,
Team Spotless
'''

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email='my.spotless.app@gmail.com',
        to=[user.email],
        reply_to=['my.spotless.app@gmail.com'],
    )
    mail.content_subtype = "html"
    mail.send()


def send_booking_confirmation(user, booking):
    subject = f'[{booking.id}] {booking.service.name}'
    message = f'''
Hi {user.first_name},

'We received your booking!'
'Someone will contact you shortly.'

For questions, please contact us via email'
' at <strong>info@spotless.se</strong> or'
' call us at <strong>0754981234</strong>.'

Best regards,
Team Spotless
'''

    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email='my.spotless.app@gmail.com',
        to=[user.email],
        reply_to=['my.spotless.app@gmail.com'],
    )
    mail.content_subtype = "html"
    mail.send()
