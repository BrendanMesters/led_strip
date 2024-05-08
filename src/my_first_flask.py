from flask import Flask
from flask import render_template

from src.controller import turn_leds_off 
from src.controller import set_leds_colour 
from src.controller import led_thread 

from queue import Queue 
from threading import Thread 



app = Flask(__name__)
led_queue = Queue()

scalar = 0.3
colour = "off"

@app.route("/")
def hello_world():
    return render_template('leds_main.html')


@app.route("/off")
def turn_off_lights():
    turn_leds_off()
    return render_template('leds_main.html', colour="off")

@app.route("/colour/<_colour>")
def change_light_colour(_colour):
    global scalar
    global colour
    colour = _colour
    set_leds_colour(colour, scalar=scalar)
    return render_template('leds_main.html', colour=colour, scalar=scalar)

@app.route("/set_scalar/<_scalar>")
def change_scalar(_scalar):
    try:
        int_scalar = float(_scalar)
    except (TypeError, ValueError):
        return render_template('leds_main.html', error= "Provided value was not an integer")
    global scalar
    global colour
    scalar = int_scalar
    set_leds_colour(colour, scalar=scalar)
    return render_template('leds_main.html', colour=colour, scalar=scalar)

if __name__ == "__main__":
    lt = Thread(target = led_thread, args = (led_queue,))
    print("about to start")
    lt.start()
    app.run(host='0.0.0.0', port=80)
