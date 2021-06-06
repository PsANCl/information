from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    """配置项目信息"""
    DEBUG = True
    # 配置数据库
    SQLALCHMEY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information28"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_POST = '6379'

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_POST)
# 开启当前项目CSRF保护，只做服务器验证功能
CSRFProtect(app)


@app.route('/')
def index():

    return "index"


if __name__ == '__main__':
    app.run()
