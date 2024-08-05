import os
import sys
import shutil
import zipfile
import tempfile
import importlib.resources as resources
from flask import Flask
from jinja2 import PackageLoader, ChoiceLoader
from werkzeug.middleware.shared_data import SharedDataMiddleware
from zipappdemo import api
from zipappdemo.config import Setting


def extract_resources(zip_path, resource_name):
    # 提取资源到临时目录
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 提取指定的目录内容
        for file in zip_ref.namelist():
            if file.startswith(resource_name):
                # 提取文件
                zip_ref.extract(file, temp_dir)
    # 构建临时目录的路径
    return os.path.join(temp_dir, resource_name)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Setting)

    ##### 方式一 加载模板和静态资源文件
    # 使用PackageLoader加载模板
    # 它能够从压缩包中加载模板文件
    #app.jinja_loader = ChoiceLoader([PackageLoader(__name__, 'templates')])
    # 共享.pyz文件外的静态资源文件
    #app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/static': 'static'})

    ##### 方式二 加载模板和静态资源文件
    # 提取静态文件和模板文件到临时目录
    static_folder = extract_resources(sys.argv[0], 'zipappdemo/static')
    template_folder = extract_resources(sys.argv[0], 'zipappdemo/templates')
    app.static_folder = static_folder
    app.template_folder = template_folder

    ## 注册蓝图
    app.register_blueprint(api.bp)

    return app


def main():
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"]
    )


if __name__ == "__main__":
    main()
