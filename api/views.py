
from api.validators import validate_params
from database.database import search_for_form


def check_form_exists(params: dict) -> dict:
    verified_params = validate_params(params)
    form_name = search_for_form(verified_params)
    if form_name:
        return {'name': form_name}
    return verified_params
