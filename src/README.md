# Python Light controller

So, the general idea for this project is to write a flexible controller for my neopixel led strip,

This controller is ran on my raspberry pi 3.



### Notes

**Flask**: The program should probably be accessible from a website, so that I can also controll my LED's 
easily from my phone, for this I'm currently trying out flask.

To run the flask (development) website in such a way that other machines on the local network
can access it we need to run the command `flask --app my_app rn --host=0.0.0.0`, the last part
makes sure that the website is exposed to the LAN.
Running the flask app with the `--debug` flag will allow flask to detect code base changes and will
have it auto update. 

_note_, running Flask apps in development mode (as I am doing right now) is not recommended
for final applications, might wanne look into how to fix that some day.
