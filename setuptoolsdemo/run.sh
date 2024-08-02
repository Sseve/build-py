#!/usr/bin/bash

## 运行脚本
## 在实际部署时, 部署的路径中包如下文件:
##     1. .env
##     2. run.bash
##     3. setuptoolsdemo-0.0.1-py3-none-any.whl

# 安装名字
project_name=setuptoolsdemo
# 安装路径
project_path=/opt/setuptoolsdemo
# 安装包名
project_packge=setuptoolsdemo-0.0.1-py3-none-any.whl
# 安装包源
pkg_source=http://mirrors.aliyun.com/pypi/simple

# 设置环境变量
export PATH=$PATH:$project_path/bin
export PYTHONPATH=$project_path

if [ -d $project_path ];then
    $project_name
else
    echo "Please: pip install $project_packge -t $project_path -i $pkg_source"
fi
