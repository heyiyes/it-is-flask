from flask import Blueprint

bp = Blueprint("goods",__name__,url_prefix='/')

@bp.route("/")
def goods():
    return "首页"