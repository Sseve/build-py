### example

* [部署]
- 方式一:
1. 直接将项目源码部署到主机上
2. 将项目的依赖安装到项目根目录的vendor目录下  
   python -m pip install -r requirements.txt -t vendor
3. 设置PYTHONPATH环境变量: export PYTHONPATH=vendor  
   注意: 该环境变量要与运行项目在同一个shell中
4. 运行项目: python -m src.example

- 方式二:
1. 编写setup.py脚本  
2. 打包(一定需要: `src/example/__init__.py`, 否则打包后找不到example包):  
   a. python setup.py sdist    (源码打包)  
      打包后的文件适用于开发者或者需要修改源码的人  
   b. python setup.py bdist_wheel    (二进制打包)  
      打包后的文件适用于直接部署  
3. 安装：
   a. python -m pip install example-0.0.1.tar.gz -t TARGET_PATH  
      运行: export PYTHONPATH=$TARGET_PATH && python -m example  
   b. python -m pip install example-0.0.1-py3-none-any.whl -t TARGET_PATH  
      运行: export PYTHONPATH=$TARGET_PATH && python -m example  
            或者 export PATH=$PATH:$TARGET_PATH/bin && example  
