from flask import Flask,session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
# 可以用来指定session保存的位置
from flask_session import Session
from flask_script import Manager


class Config(object):
    """配置项目信息"""
    DEBUG = True

    SECRET_KEY = "iECgbYWReMNxkRprrzMo5KAQYnb2UeZ3bwvReTSt+VSESW0OB8zbglT+6rEcDW9X"

    # 配置数据库
    SQLALCHMEY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information28"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_POST = '6379'
    # session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_POST)
    # 设置需要过期时间
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_POST)
# 开启当前项目CSRF保护，只做服务器验证功能
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

manager = Manager(app)


@app.route('/')
def index():
    session["name"] = "itheima"
    return "index"


if __name__ == '__main__':
    manager.run()
