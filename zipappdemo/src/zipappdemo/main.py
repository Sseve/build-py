from zipappdemo import create_app
from gunicorn.app.base import BaseApplication


class Application(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application


def main():
    app = create_app()

    #app.run(
    #    host=app.config["HOST"],
    #    port=app.config["PORT"]
    #)

    options = {
        "workers": app.config["WORKERS"],
        "timeout": app.config["TIMEOUT"],
        "pidfile": app.config["PIDFILE"],
        "bind": f"{app.config['HOST']}:{app.config['PORT']}",
    }
    # ## 运行模式
    try:
        Application(app, options).run()
    except Exception:
        pass


if __name__ == "__main__":
    main()
