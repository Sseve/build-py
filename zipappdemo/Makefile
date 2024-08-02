# zipapp构建demo项目
# 安装依赖: .venv/bin/python -m pip install -r requirements.txt

PYTHON := .venv/bin/python
ENVPYTHON := "/usr/bin/env python"
BUILD := build
TARGET := zipappdemo.pyz
SRC := src/zipappdemo
ENTRYPOINT := zipappdemo.main:main
LIBS := .venv/lib/python3.10/site-packages/*

.PHONY: all clean

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	cp -r $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -p $(ENVPYTHON) -c -m $(ENTRYPOINT) -o $(TARGET)

clean:
	rm -fr $(BUILD) $(TARGET)
