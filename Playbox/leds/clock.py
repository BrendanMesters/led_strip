import time
from datetime import datetime

# returns a greycode of 2^n bits
def get_gray(n):
    if n == 1:
        return [(), (0,)]
    else:
        oldval = get_gray(n-1)
        retval = oldval + oldval[::-1]
        #print(f"in gray code{n} we have preretval {retval}")
        for i in range((2**(n-1)), 2**n):
            retval[i] = retval[i] + (n-1,)
    return retval



def main():
    now = datetime.now()
    six_gray = get_gray(6)
    five_gray = get_gray(5)
    #the pi seems to grab GMT and we're GMT +1
    time = (now.hour + 1, now.minute, now.second)
    print(f"""The time in greycode is \n {five_gray[time[0]]} hours ({time[0]})
                                    \n {six_gray[time[1]]} minutes ({time[1]}) 
                                    \n {six_gray[time[2]]} seconds ({time[2]})""" )




if __name__ == "__main__":
    main()

