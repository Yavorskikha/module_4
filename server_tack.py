from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies


@route("/")
@view("predictions_test")
def index():
  now = dt.now()
  x = random()
  
  return {
  "date": f"{now.year}-{now.month}-{now.day}",
  "predictions": generate_prophecies(),
  "special_date": x > 0.5,
  "x": x,
  }



@route("/api/forecasts")
def api_test():
      return {"prophecies": generate_prophecies()}
   
run(
	host="https://yavorskikha.github.io/module_4/", 
	port=8080, 
	debug=True,
	reloader = True
)