from flask import Flask, redirect, render_template
from dotenv import load_dotenv
from os import getenv

load_dotenv()




app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/login")
@app.route("/auth")
def login_handler():
    return render_template("auth.html")

@app.errorhandler(404)
def redirect_to_google(e):
    print(str(e))
    return redirect("https://google.com")


if __name__ =="__main__":
    debug_status = False
    environment = getenv("ENVIRONMENT")
    if environment == "production":
        debug_status = False
    else:
        environment= "development"
        debug_status=True


    app.run(
        host="0.0.0.0",
        port=9000,
        debug=debug_status,
        threaded = True,
        use_reloader=True,
        passthrough_errors=False
    )  