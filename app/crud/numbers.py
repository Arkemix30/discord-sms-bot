from ..core.db import get_session
from ..core.loggin_config import get_logger
from ..models import Numbers
from ..schemas.register import RegisterSchema
from ..utils.queries.numbers import get_number

logger = get_logger(__name__)


class CRUDNumber:
    def __init__(self, model: Numbers):
        self.model = model
        self.db = get_session()

    def register_number(self, new_number: RegisterSchema):
        with self.db as session:
            number_in_db = get_number(session, new_number)
            if number_in_db:
                if number_in_db.is_active:
                    date = number_in_db.created_at.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    return (
                        f"Number: {new_number.number}"
                        f" was already registered by: `{number_in_db.created_by}`"
                        f" at: {date} UTC"
                    )
                else:
                    number_in_db.is_active = True
                    session.add(number_in_db)
                    session.commit()
                    session.refresh(number_in_db)
            else:
                number = self.model(**new_number.dict())
                try:
                    session.add(number)
                    session.commit()
                except Exception as err:
                    msg_error = "❌ERROR❌\nError while inserting new number into database"
                    logger.error(f"{msg_error}, error: {err}")
                    return msg_error
        return (
            f"Number: {new_number.number}"
            f" was   by User: `{new_number.created_by}`"
        )

    def unregister_number(self, existing_number: RegisterSchema):
        with self.db as session:
            result = get_number(session, existing_number)

        if not result:
            msg_error = "❌ERROR❌\nNumber not found"
            logger.error(msg_error)
            return msg_error

        try:
            result.is_active = False
            with self.db as session:
                self.db.add(result)
                self.db.commit()
        except Exception as err:
            msg_error = "❌ERROR❌\nError while trying to unregister number"
            logger.error(f"{msg_error}, error: {err}")
            return msg_error
        return (
            f"Number: {existing_number.number}"
            f" was successfully unregistered by User: `{existing_number.created_by}`"
        )


numbers_crud = CRUDNumber(Numbers)
