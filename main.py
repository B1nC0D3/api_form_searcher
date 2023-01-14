from fastapi import Body, FastAPI

from api.views import check_form_exists

app = FastAPI()


@app.post('/get_form/')
def get_form(params: dict = Body(...)):
    return check_form_exists(params)
