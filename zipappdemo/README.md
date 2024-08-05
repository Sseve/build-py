### zipapp demo

python 标准库 zipapp 进行打包

打包: make  
清理: make clean  

方式一部署: 将打包文件与静态资源文件一起部署到目标主机上
``` 
deploy/
|-- .env
|-- static
|   `-- css
|       `-- index.css
`-- zipappdemo.pyz
```

方式二部署: 将打包文件部署到目标主机上
```
deploy/
|-- .env
`-- zipappdemo.pyz
```
运行: python zipappdemo.pyz  
