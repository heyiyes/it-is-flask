from flask import Flask
import config
from exts import db
from blueprints import goods_bp
from blueprints import user_b_bp
from blueprints import user_u_bp

app = Flask(__name__)
# 以后所有的配置项都会放到config中
app.config.from_object(config)
db.init_app(app)


app.register_blueprint(goods_bp)
app.register_blueprint(user_b_bp)
app.register_blueprint(user_u_bp)


if __name__ == '__main__':
    app.run()
