# zip命令打包

SRC = app/
DEP = /tmp/zipdemo/
DST = demo.pyz

.PHONY: build,clean

build:
	python -m pip install -r requirements.txt -t $(DEP)
	zip -9 -r $(DST) $(SRC) $(DEP) __main__.py

clean:
	rm $(DST) $(DEP) -fr