NAME := zipappdemo
PYTHON := .venv/bin/python
BUILD := build
TARGET := $(NAME).pyz
SRC := src/$(NAME)
ENTRYPOINT := $(NAME).main:main
LIBS := .venv/lib/python3.10/site-packages/*

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)
	cp -r $(SRC) $(BUILD)
	rsync -a --exclude='__pycache__' --exclude='templates' --exclude='static' $(LIBS) $(BUILD)
	$(PYTHON) -m zipapp $(BUILD) -m $(ENTRYPOINT) --compress -o $(TARGET)

.PHONY: all clean

clean:
	rm -fr $(BUILD) $(TARGET) 
