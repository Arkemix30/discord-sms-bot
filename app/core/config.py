import os

from dotenv import load_dotenv

from app.core.loggin_config import get_logger

logger = get_logger(__name__)
load_dotenv(override=True)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_NAME = os.environ.get("DB_NAME")

SMS_PROVIDER = os.environ.get("SMS_PROVIDER")


def get_db_uri():
    return (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


def get_message_config(sms_provider: str = SMS_PROVIDER):
    if sms_provider.lower() == "twilio":
        twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        twilio_messaging_service_sid = os.environ.get(
            "TWILIO_MESSAGING_SERVICE_SID"
        )
        twilio_notify_service = os.environ.get("TWILIO_NOTIFY_SERVICE")
        if (
            not twilio_account_sid
            or not twilio_auth_token
            or not twilio_messaging_service_sid
        ):
            msg_error = "TWILIO_ACCOUNT_SID/TWILIO_AUTH_TOKEN/TWILIO_MESSAGING_SERVICE_SID not found in environment variables"
            logger.error(msg_error)
            raise Exception(msg_error)

        return {
            "sms_provider": sms_provider.lower(),
            "account_sid": twilio_account_sid,
            "auth_token": twilio_auth_token,
            "messaging_service_sid": twilio_messaging_service_sid,
            "notify_service": twilio_notify_service,
        }

    messagebird_access_key = os.environ.get("MESSAGEBIRD_ACCESS_KEY")

    if not messagebird_access_key:
        msg_error = (
            "MESSAGEBIRD_ACCESS_KEY not found in environment variables"
        )
        logger.error(msg_error)
        raise Exception(msg_error)

    return {
        "sms_provider": sms_provider.lower(),
        "access_key": messagebird_access_key,
    }
