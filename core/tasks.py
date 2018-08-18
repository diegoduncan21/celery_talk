import logging
from time import sleep

from django.core.mail import send_mail

from celery_app import app


logger = logging.getLogger('core.tasks')


@app.task
def test_task(a, b):
    print "LALALALA"  # NO
    logger.info("LALALAL")  # SI
    return a + b


@app.task
def test_task_2(user):
    sleep(10)
    return 0


@app.task
def test_task_3(a, b):
    """ A Task with an error. """
    return a / b


@app.task(ignore_result=True, time_limit=10 * 60)
def send_registration_email(user):
    """ Account confirmation """

    subject = 'un subject'
    message = 'un mensaje'
    from_email = 'diegoduncan21@gmail.com'
    return send_mail(subject, message, from_email, ['un@mail.com'])
