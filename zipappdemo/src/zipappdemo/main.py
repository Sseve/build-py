from flask import Flask
from .config import Setting


def create_app():

    app = Flask(__name__)
    app.config.from_object(Setting)


    @app.route("/", methods=("GET", "POST"))
    def test():
        return {"hello": "world"}

    return app


def main():
    app = create_app()

    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"]
    )


if __name__ == "__main__":
    main()
