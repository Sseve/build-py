# shiv打包
# python -m pip install shiv -t /opt/app
# export PYTHONPATH=/opt/app:.venv/lib/python3.10/site-packages/

.PHONY: build,clean

build:
	python -m shiv -o demo.pyz -e shivdemo.main:main -r requirements.txt --compressed --site-packages src --root /tmp/shiv

clean:
	rm demo.pyz -fr
