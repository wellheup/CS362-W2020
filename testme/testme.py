import random
import time
import atexit


# Piazza post @152
start_time = time.time()
@atexit.register
def goodbye():
    print("Program ran in %.2f seconds (%.2f minutes)" % ((time.time() - start_time), (time.time() - start_time)/60))


def inputChar():
    c = chr(random.randrange(32, 126))
    return c


def inputString():
    s = ""
    for i in range(5):
        s += chr(random.randrange(97, 123))
    return s


def testme():
    tcCount = 0
    state = 0
    while 1:
        tcCount += 1
        c = inputChar()
        s = inputString()
        print("Iteration %d: c = %c, s = %s, state = %d" % (tcCount, c, s, state))

        if c == '[' and state == 0:
            state = 1
        if c == '(' and state == 1:
            state = 2
        if c == '{' and state == 2:
            state = 3
        if c == ' ' and state == 3:
            state = 4
        if c == 'a' and state == 4:
            state = 5
        if c == 'x' and state == 5:
            state = 6
        if c == '}' and state == 6:
            state = 7
        if c == ')' and state == 7:
            state = 8
        if c == ']' and state == 8:
            state = 9
        if s == "reset" and state == 9:
            print("error")
            exit(200)


random.seed()
testme()