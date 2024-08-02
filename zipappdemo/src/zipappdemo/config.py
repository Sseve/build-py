import os
from dotenv import load_dotenv


# 加载配置
if os.path.exists(".env"):
    load_dotenv(".env")
else:
    raise FileNotFoundError(".env Not Found! please config it in current path.")


class Setting:
    """.env配置"""
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
