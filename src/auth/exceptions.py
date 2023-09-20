from auth.constants import ErrorCode
from exceptions import BadRequest


class EmailExists(BadRequest):
    DETAIL = ErrorCode.EMAIL_EXISTS
