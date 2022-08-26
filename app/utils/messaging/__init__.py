from app.core.config import get_message_config

from .messagebird_messages import messagebird_send_sms
from .twilio_messages import twilio_send_sms


def send_sms(
    to_numbers: list[str],
    body: str,
    sms_provider=get_message_config().get("sms_provider"),
):
    if sms_provider == "twilio":
        return twilio_send_sms(to_numbers, body)
    else:
        return messagebird_send_sms(to_numbers, body)
