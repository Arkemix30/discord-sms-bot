from datetime import datetime as dt

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from app.core.config import get_message_config
from app.core.loggin_config import get_logger
from app.utils.utils_general import serialize_number_addresses

logger = get_logger(__name__)
config = get_message_config()

account_sid = config.get("account_sid")
auth_token = config.get("auth_token")
messaging_service_sid = config.get("messaging_service_sid")
notify_service = config.get("notify_service")
client = Client(account_sid, auth_token)


def twilio_send_sms(to_numbers: list[str], body: str):
    try:
        binding_list = serialize_number_addresses(to_numbers)

        logger.info(
            f"Sending SMS to {to_numbers} at {dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        client.notify.services(notify_service).notifications.create(
            to_binding=binding_list, body=body
        )

    except TwilioRestException as err:
        msg_error = f"❌ERROR❌\nError when trying to send sms, error: {err}"
        logger.error(msg_error)
        return {"error": msg_error}

    return {"data": "SMS sent successfully"}
