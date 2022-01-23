from flask import Blueprint

bp = Blueprint("user_u",__name__,url_prefix='/user')

@bp.route("/behind")
def behind():
    return "后台"