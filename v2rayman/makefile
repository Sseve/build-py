# 直接用zip命令压缩文件打包
# 保证项目的入库文件命名为: __main__.py

.PHONY: build,clean

build:
	@mkdir build
	@cp -r .venv/lib/python3.11/site-packages/* build
	@cp -r src/example/* build
	@cd build && zip -9 -r example.pyz ./* && mv example.pyz ..

clean:
	@rm -fr build example.pyz
