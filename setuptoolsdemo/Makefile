# setuptools打包项目
# 查看帮助信息: python setup.py --help-command
# 安装: python -m pip install wheel setuptools \
#   -i http://mirrors.aliyun.com/pypi/simple \
#   --trusted-host mirrors.aliyun.com

# 打包: PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple python -m build -v
# 安装: python -m pip install . -t /opt/setuptoolsdemo/ -i https://pypi.tuna.tsinghua.edu.cn/simple

SCRIPT := setup.py
PYTHON := /usr/bin/python
TARGET := build dist src/setuptoolsdemo.egg-info

build:
	$(PYTHON) $(SCRIPT) bdist_wheel

.PHONY: all clean

clean:
	rm -fr $(TARGET)

## 安装到指定目录:
##    pip install setuptoolsdemo-0.0.1-py3-none-any.whl -t path_name
## 运行安装后的包:
##    1. export PYTHONPATH=$PYTHONPATH:path_name
##    2. $path_name/setuptoolsdemo
