from flask import Blueprint

bp = Blueprint("user_b",__name__,url_prefix='/user')

@bp.route("/login")
def login():
    return "登录"