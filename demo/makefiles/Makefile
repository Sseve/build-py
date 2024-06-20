# 标准库zipapp打包项目源代码.
# 如果项目源码中的入口文件main.py命名是__main__.py,
# 则这里zipapp不需要设置-m参数(对比zipapp.mk文件):
#    -m demo.__main__:main
# 否则会报错!!!!!!!!

.PYONY: clean

OUT := demo.pyz
SRC := src/demo/*
LIB := .venv/lib/python3.10/site-packages/*
BUILD := build
PYTHON := .venv/bin/python
ENVPYTHON := "/usr/bin/env python"

build:
	[ ! -d $(BUILD) ] && mkdir $(BUILD)

	# copy src
	cp -r $(SRC) $(BUILD)

	# copy lib
	cp -r $(LIB) $(BUILD)

	# packge build
	$(PYTHON) -m zipapp $(BUILD) -p $(ENVPYTHON) -c -o $(OUT)

clean:
	rm -fr $(OUT) $(BUILD)
