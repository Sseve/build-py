import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/test")
def test():
    return "hello world"


def main():
    uvicorn.run("src.v2rayman.run:app", host="0.0.0.0", port=8887)


if __name__ == "__main__":
    main()
