### venv

* [说明]
- python项目如何在不启用隔离环境就使用隔离环境中的三方依赖包
1. 新建隔离环境: python -m venv vendor
2. 设置PYTHONPATH变量: export PYTHONPATH=vendor/lib/python3.10/site-packages
