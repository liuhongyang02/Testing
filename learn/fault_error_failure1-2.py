import re
import thread
import time
def findElements(lines):
    try:
        document = open("testfile","r")
        readfile = document.readlines()
        le = []
        a = []
        for line in readfile:
            le.append(re.split(" ",line.strip()))
        #change value
        a = le[lines]
        size = len(a)
        b = "w"
        if (size <= 1):
            if (b == a[0]):
                pos = 1
            else:
                pos = -1
        else:
            pos = -1
            for i in range(1, size):
                if (b == a[i]):
                    pos = i + 1
                    break;
        print "string array is:\n"
        for i in range(0, size):
            print a[i],
        print "first element\' position is:%s" % pos
        document.close()
    except IOError:
        print 'i can\'t read this file'

try:
    thread.start_new_thread(findElements, (0,))
    time.sleep(1)
    thread.start_new_thread(findElements, (1,))
    time.sleep(1)
    thread.start_new_thread(findElements, (2,))
except IOError:
    print "unable to start thread"
while 1:
    pass