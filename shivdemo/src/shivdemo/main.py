import uvicorn
from fastapi import FastAPI

from .api import demo


app = FastAPI()


def main():
    app.include_router(demo.router, prefix='/api')

    uvicorn.run("shivdemo.main:app", host="0.0.0.0", port=9999)



if __name__ == "__main__":
    main()