# zipapp构建demo项目
# 安装依赖: .venv/bin/python -m pip install -r requirements.txt

NAME := zipappdemo
PYTHON := .venv/bin/python
BUILD := build
TARGET := $(NAME).pyz
SRC := src/$(NAME)
ENTRYPOINT := $(NAME).main:main
LIBS := .venv/lib/python3.10/site-packages/*
DEPLOY := deploy

.PHONY: all clean

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	#cp -r $(LIBS) $(BUILD)
	# --exclude='*.dist-info/' 不能排除
	rsync -a --exclude='__pycache__' $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -m $(ENTRYPOINT) -c -o $(TARGET)

	[ ! -d $(DEPLOY) ] && mkdir $(DEPLOY)
	cp .env $(TARGET) $(DEPLOY)
	rsync -a src/$(NAME)/static $(DEPLOY)
	tar -czf $(DEPLOY).tar.gz $(DEPLOY)

clean:
	rm -fr $(BUILD) $(TARGET) $(DEPLOY)
