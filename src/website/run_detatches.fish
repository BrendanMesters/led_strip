#!/bin/fish
nohup flask --app my_first_flask run --host=0.0.0.0 --debug >> flask_output.txt &
