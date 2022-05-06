
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Home():
    return {"data": "Hello Flask!"}

@app.route("/current_datetime")
def Current_datetime():
    now = datetime.today()
    return {
  "current_datetime": now.strftime("%d/%m/%Y %I:%M:%S %p"),
  "message": "Boa tarde!"
}
