import os
from flask import Flask
from jinja2 import PackageLoader, ChoiceLoader
from werkzeug.middleware.shared_data import SharedDataMiddleware
from zipappdemo import api
from zipappdemo.config import Setting


def create_app():

    app = Flask(__name__, static_folder='static')
    app.config.from_object(Setting)

    # 使用PackageLoader加载模板
    # 它能够从压缩包中加载模板文件
    package_loader = PackageLoader(__name__, 'templates')
    app.jinja_loader = ChoiceLoader([package_loader])
    # 共享.pyz文件外的静态资源文件
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/static': 'static'})

    app.register_blueprint(api.bp)

    return app


def main():
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"]
    )


if __name__ == "__main__":
    main()
