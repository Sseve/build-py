FROM python:3.10.14-alpine3.20

WORKDIR /app

# 创建并切换到新的用户
#RUN useradd abc -s /sbin/nologin
#USER abc

# 使用默认已有用户
USER nobody

COPY --chown=nobody:nobody demo.pyz .env .

CMD ["python", "demo.pyz"]
