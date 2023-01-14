from enum import Enum


class FieldType(str, Enum):
    date = 'DATE'
    phone = 'PHONE'
    email = 'EMAIL'
    text = 'TEXT'
