import matplotlib.pyplot as plt
import random
import _thread
import time

x = []
y = []
def fun():

    #print("hello World")
    #for i in range(20):
    #    print("Hello Egypt")
    plt.ion()
    plt.gca().set_ylim([0, 500])
    plt.show()
    for i in range(40):
        plt.pause(1e-12)
        print("hello world")
        x.append(i)
        y.append(int(random.random() * 100))
        plt.plot(x, y)
    #plt.ioff()
    #plt.show()

_thread.start_new_thread(fun,tuple())
for i in range(100):
    print("Hello Egypt")
    time.sleep(1)

while 1:
    pass