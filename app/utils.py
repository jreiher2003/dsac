from app import app, mail
from flask import request
from urlparse import urlparse, urljoin
from flask_mail import Message 

def contact_form_email(message, sender):
    msg = Message(
        subject="EMAIL CONTACT FORM",
        recipients=["jeffreiher@gmail.com"],
        body=message,
        sender=sender
    )
    mail.send(msg)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc