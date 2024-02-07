"""
LED CONTROLLER

Consumes multiple led modules, receives the generated LED data from each 
module, combines them into one 300 pixel wide signal (representing the 
whole LED strip) and writes the information to the LED strips.

I might want to think about generalizable ways in which I can interact with 
modules, the most straight forewards being POLLING, however, data pre-generation
and working with shared queue-dequeues is something to look at lateron.

At first we will probably hard code all the different parts.


 -= Brendan Mesters =-
https://github.com/BrendanMesters
-=-=-=-=-=-=-=-=-=-=-=-=-
"""

