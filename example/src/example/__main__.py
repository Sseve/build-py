import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def hello():
    return "hello fastapi"


def main():
    # 方式一源码运行时
    # uvicorn.run("__main__:app", host="0.0.0.0", port=6666)

    # 注意: example.__main__:app, 会影响打包后的运行,
    # 特别是README.md中方式二中的b运行方式.
    uvicorn.run("example.__main__:app", host="0.0.0.0", port=6666)


if __name__ == "__main__":
    main()
