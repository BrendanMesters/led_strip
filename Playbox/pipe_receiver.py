import time


f = open("../communication_infrastructure/channel.fifo", mode = "r")
while True:
    try:
        print(len(f.read()))
    finally:
        time.sleep(1)