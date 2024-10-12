# 打包项目
NAME := v2rayman

build:
	pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple 
	python -m zipapp . -o $(NAME).pyz -m "src.v2rayman.run:main" --compress

clean:
	rm $(NAME).pyz
