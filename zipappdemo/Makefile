# zipapp构建demo项目
# 安装依赖: .venv/bin/python -m pip install -r requirements.txt

NAME := zipappdemo
PYTHON := .venv/bin/python
BUILD := build
TARGET := $(NAME).pyz
SRC := src/$(NAME)
ENTRYPOINT := $(NAME).main:main
LIBS := .venv/lib/python3.10/site-packages/*

.PHONY: all clean

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	#cp -r $(LIBS) $(BUILD)
	# --exclude='*.dist-info/' 不能排除
	rsync -a --exclude='__pycache__' $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -c -m $(ENTRYPOINT) -o $(TARGET)

clean:
	rm -fr $(BUILD) $(TARGET)
