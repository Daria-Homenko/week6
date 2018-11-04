from flask import Blueprint
from flask.views import MethodView

from db.db_app import db

create_db = Blueprint('create_db', __name__, static_folder='../../static', template_folder='../../template')


class CreateDatabase(MethodView):

    def post(self):
        try:
            db.create_all()
            db.session.commit()
            return "Successfully created all tables"
        except:
            return "Fail created all tables"


create_db.add_url_rule('/db', view_func=CreateDatabase.as_view('create_db'))
