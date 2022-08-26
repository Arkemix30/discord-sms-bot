from datetime import datetime as dt

from app.utils.messaging import send_sms

from ..core.db import get_session
from ..core.loggin_config import get_logger
from ..models import Notifications, Numbers, NumbersNotifications
from ..utils.queries.numbers import get_all_active_numbers

logger = get_logger(__name__)


class CRUDNotifications:
    def __init__(self):
        self.db = get_session()

    def send_sms(self, body: str, user: str):
        with self.db as session:
            numbers_list_results = get_all_active_numbers(session)

        if len(numbers_list_results) == 0:
            return "There are not any active numbers"
        to_numbers = [number.number for number in numbers_list_results]

        sms_result = send_sms(to_numbers, body)
        if sms_result.get("error"):
            return sms_result.get("error")

        with self.db as session:
            notification = Notifications(message=body, sent_by=user)
            try:
                session.add(notification)
                session.commit()
                session.refresh(notification)
            except Exception as err:
                msg_error = "❌ERROR❌\nError while inserting notification into database"
                logger.error(f"{msg_error}, error: {err}")
                return msg_error

        with self.db as session:
            try:
                for number in numbers_list_results:
                    number_notification = NumbersNotifications(
                        number_id=number.id, notification_id=notification.id
                    )
                    session.add(number_notification)
                session.commit()
            except Exception as err:
                msg_error = "❌ERROR❌\nError while inserting NumbersNotifications into database"
                logger.error(f"{msg_error}, error: {err}")
                return msg_error
        return f"SMS was successfully sent by User: `{notification.sent_by}`"


notification_crud = CRUDNotifications()
