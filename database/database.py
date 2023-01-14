from tinydb import TinyDB, Query


db = TinyDB('database/db.json')
Forms = db.table('FORMS')
q = Query()


def search_for_form(incoming_form: dict) -> str:
    form = Forms.search(q.fragment(incoming_form))
    if form:
        return form[0].get('name')
    return ''
