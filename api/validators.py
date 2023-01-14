import re
from datetime import datetime

from fastapi import HTTPException, status

from api.models import FieldType


def raise_exception(detail: str):
    raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=detail)


def validate_date(date: str):
    if '.' in date:
        try:
            datetime.strptime(date, '%d.%m.%Y')
        except ValueError:
            raise_exception('Неверная дата')
    else:
        try:
            datetime.fromisoformat(date)
        except ValueError:
            raise_exception('Неверная дата')


def validate_phone(phone: str):
    if not re.match(r'(?:\+7) \d{3} \d{3} \d{2} \d{2}$', phone):
        raise_exception('Неверный номер телефона')


def validate_email(email: str):
    if not re.match(r'^[-\w\.]+@[-\w\.]+\.\w{2,5}$', email):
        raise_exception('Неверный email')


def validate_params(params: dict):
    verified_params = {}
    dates_regex = (r'\d\d\.\d\d\.\d{4}$', r'\d{4}-\d\d-\d\d$')
    date = re.compile('|'.join(dates_regex))
    for key, value in params.items():
        if date.match(value):
            validate_date(value)
            verified_params[key] = FieldType.date.value
        elif re.search(r'^\+7 \d{3} ', value):
            validate_phone(value)
            verified_params[key] = FieldType.phone.value
        elif re.search(r'\w@\w', value):
            validate_email(value)
            verified_params[key] = FieldType.email.value
        else:
            verified_params[key] = FieldType.text.value
    return verified_params
