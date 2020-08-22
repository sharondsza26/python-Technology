# stage 1
from threading import *

import time



class TestBed:

    def busyTracks(self):
        t = current_thread()
        #whichever thread enters first, thhat threads obj will be loaded in var t
        print("{} Entered Busy Tracks".format(t.name))

        lap = 0     #Local Variable

        while(lap < 5):

            if(t.name == "Car"): print("brrrommsss")

            else: print("vrrrommsss")

            time.sleep(1)   #sleeping for 1 sec
            lap += 1
            print("Lap = {}".format(lap))

        print("{} Leaving Busy Tracks".format(t.name))





class Bike(Thread):
    # standard procedure
    def __init__(self):
        Thread.__init__(self,name="Bike")

    def run(self):

        print("Bike Starts Journey")
        TestBed().busyTracks()
        # creating obj of class TestBed and calling busyTracks method
        print("Bike Ends Journey")





class Car(Thread):
    # standard procedure
    def __init__(self):
        Thread.__init__(self,name="Car")

    def run(self):

        print("Car Starts Journey")
        TestBed().busyTracks()
        # creating obj of class TestBed and calling busyTracks method
        print("Car Ends Journey")



Car().start()
# ^ car object
# c = Car()
# c.start


Bike().start()