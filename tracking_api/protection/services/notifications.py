from typing import Union

from protection.models import Task
from users.models import Client, Worker


def send_email(email: str, text: str) -> None:
    print(f'email: {email} text: {text}')


def send_sms(phone: str, text: str) -> None:
    print(f'phone: {phone} text: {text}')


def send_in_app(user_id: int, text: str) -> None:
    print(f'user_id: {user_id} text: {text}')


def send_call(phone: str, text: str) -> None:
    print(f'phone: {phone} text: {text}')


def send_notification(recipient: Union[Worker, Client], task: Task) -> None:
    settings = recipient.notification_settings
    content = task.name
    contacts = recipient.contact

    if settings.receive_call:
        send_call(contacts.phone, content)
    if settings.receive_email:
        send_email(contacts.email, content)
    if settings.receive_sms:
        send_sms(contacts.phone, content)
    if settings.receive_app_notification:
        send_in_app(recipient.id, content)






