from flask import Blueprint, redirect
from flask.views import MethodView


class ApiView(MethodView):
    def get(self):
        return redirect('/login')



api = Blueprint('api', __name__, static_folder='./static', template_folder='./template')

api.add_url_rule('/api', view_func=ApiView.as_view('api'))
