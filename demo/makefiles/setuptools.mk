# setuptools打包项目
# 查看帮助信息: python setup.py --help-command
# 安装: python -m pip install wheel setuptools \
#   -i http://mirrors.aliyun.com/pypi/simple \
#   --trusted-host mirrors.aliyun.com

SCRIPT := setup.py
PYTHON := /usr/bin/python
TARGET := build dist src/demo.egg-info

build:
	$(PYTHON) $(SCRIPT) bdist_wheel

.PHONY: all clean

clean:
	rm -fr $(TARGET)
