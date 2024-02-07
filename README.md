# LED strip controller

This repository is a place for me to work on my LED strip controller. 

I have a *5 meter* ledstrip with a *60 pixels per meter* density (totaling to **300** pixels).

This led strip is currently installed on my wall in a diffusing LED  holder (named, idk)

# Structure of the code

The core idea is to have a single LED stirp controller, with multiple modules

The controller would ask of the modules to provide a certain amount of information, a clock might for example only require 40 pixels, thus the clock module would only generate 40 pixels of data.

The controllers main job is to get the information of the different modules (some might require fast response times, while others might be more lax), and to "layer" the different LED commands (For example, the clock signal should take priority over background lighting).

The different modules might work with either polling or interrupts to inform the controller of their values, some controllers might also be able to queue values for the controller to read as he has time for it.

At first I will probably just pass priority around manually (calling the different modules from within controller), but lateron I will probably have to change this to work with async code and shared data structures like queue-dequeues.


I'm currenlty actually using a module from *adafruit*.
[here](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage) is the link to that

The first guide I used was [this one](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/), though the adafruit extention makes it way nicer to use (and is build on top of the one mentioned in this acticle)
