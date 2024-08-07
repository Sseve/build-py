from flask import Blueprint, render_template


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/", methods=("GET", "POST"))
def test():
    return render_template("index.html")


@bp.route("/demo", methods=("GET", "POST"))
def demo():
    return render_template("demo/demo.html")
