# pex 构建demo项目
# 安装: python -m pip install pex \
#   -i http://mirrors.aliyun.com/pypi/simple \
#   --trusted-host mirrors.aliyun.com

PEX := ~/.local/bin/pex
TARGET := demo
ENTRYPOINT := demo.main:main
PIPSOURCE := https://pypi.tuna.tsinghua.edu.cn/simple

build:
	$(PEX) -r requirements.txt -e $(ENTRYPOINT) -i $(PIPSOURCE) -D src -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(TARGET)
