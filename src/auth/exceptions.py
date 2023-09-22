from src.auth.constants import ErrorCode
from src.exceptions import BadRequest


class EmailExists(BadRequest):
    DETAIL = ErrorCode.EMAIL_EXISTS
