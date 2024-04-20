from app.shared.utils.general import ExtendedEnum


class UserRole(str, ExtendedEnum):
    USER = "user"
    ADMIN = "admin"


class UserStatus(str, ExtendedEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"


class Type(str, ExtendedEnum):
    SPEND = "spend"
    INCOME = "income"
    SAVE = "save"


class Status(str, ExtendedEnum):
    DONE = "Done"
    DRAFT = "Draft"


class Period(str, ExtendedEnum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"


class AuthGrantType(str, ExtendedEnum):
    RESET_PASSWORD = "reset_password"
    ACCESS_TOKEN = "access_token"


class GoogleSheetColor(dict, ExtendedEnum):
    RED = {"red": 1.0, "green": 0.0, "blue": 0.0}
    YELLOW = {"red": 1.0, "green": 1.0, "blue": 0.0}