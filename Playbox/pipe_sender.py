import time


f = open("../communication_infrastructure/channel.fifo", mode = "w")
while True:
    f.write("test")
    time.sleep(1)
