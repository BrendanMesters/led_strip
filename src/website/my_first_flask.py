from flask import Flask
from flask import render_template

import socket

from queue import Queue 
from threading import Thread 


def send_message(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 65432))
        s.sendall(message.encode())



app = Flask(__name__)
led_queue = Queue()

scalar = 0.3
colour = "off"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.get('/shutdown')
def shutdown():
    global app
    app.stop()
    return 'Server shutting down...'

@app.route("/")
def hello_world():
    return render_template('leds_main.html')


@app.route("/off")
def turn_off_lights():
    global scalar
    send_message(f"COLOUR OFF {scalar}")
    # turn_leds_off()
    return render_template('leds_main.html', colour="off")

@app.route("/colour/<_colour>")
def change_light_colour(_colour):
    if _colour == "gay":
        send_message("FUNCTION GAY")
        # do_the_gay()
        return render_template('leds_main.html', colour="hella gay ledstrip")
    global scalar
    global colour
    colour = _colour
    send_message(f"COLOUR {colour} {scalar}")
    # set_leds_colour(colour, scalar=scalar)
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
    send_message(f"COLOUR {colour} {scalar}")
    # set_leds_colour(colour, scalar=scalar)
    return render_template('leds_main.html', colour=colour, scalar=scalar)

if __name__ == "__main__":
    leds_thread = Thread(target = led_thread, args = (led_queue,))
    print("about to start")
    leds_thread.start()
    app.run(host='0.0.0.0', port=80)
