# pyproject.toml文件打包项目
# 依赖于: pip install --upgrade setuptools wheel build

PYTHON := /usr/bin/python

build:
	PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple $(PYTHON) -m build -v

.PHONY: all clean
clean:
	rm -rf dist/ src/builddemo.egg-info
