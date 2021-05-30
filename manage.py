from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    """配置项目信息"""
    DEBUG = True
    # 配置数据库
    SQLALCHMEY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information28"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy()

@app.route('/')
def index():

    return "index"


if __name__ == '__main__':
    app.run(debug=True)
