from brewapp import app, socketio, db
from brewapp.base.util import *
from subprocess import call

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except:
    pass


def initGPIO():
    try:
        #all(["modprobe", "w1-gpio"])
        #call(["modprobe", "w1-therm"])
        #print "###### SETUP GPIO 2 #######"
        for vid in app.brewapp_kettle_state:
            if(app.brewapp_kettle_state[vid]["heater"]["gpio"] != None):
                print "SETUP GPIO HEATER", app.brewapp_kettle_state[vid]["heater"]["gpio"]
                #GPIO.setup(int(app.brewapp_kettle[vid]["heater"]["gpio"]), GPIO.OUT)
                #GPIO.output(app.brewapp_kettle[vid]["heater"]["gpio"], 1)
            if(app.brewapp_kettle_state[vid]["agitator"]["gpio"] != None):
                print "SETUP GPIO AGITATOR", app.brewapp_kettle_state[vid]["agitator"]["gpio"]
                #GPIO.setup(app.brewapp_kettle[vid]["agitator"]["gpio"], GPIO.OUT)
                #GPIO.output(app.brewapp_kettle[vid]["agitator"]["gpio"], 1)
        app.brewapp_gpio = True
    except:
        print  "     -->GPIO SETUP FAILED"
        #app.brewapp_gpio = False

def toogle(vid, name, gpio):
    if(app.brewapp_kettle_state[vid][name]["gpio"] == gpio):
        if(app.brewapp_kettle_state[vid][name]["state"] == False):
            switchON(gpio)
            app.brewapp_kettle_state[vid][name]["state"] = True
        else:
            switchOFF(gpio)
            app.brewapp_kettle_state[vid][name]["state"]= False

def switchON(gpio):
    print "GPIO ON", gpio
    if(app.brewapp_gpio == True):
        #GPIO.output(gpio, 0)
        pass
    else:
        print "GPIO NOT READY DO SWITCH ON :", gpio

def switchOFF(gpio):
    print "GPIO OFF", gpio
    if(app.brewapp_gpio == True):
        #GPIO.output(gpio, 1)
        pass
    else:
        print "GPIO NOT READY DO SWITCH OFF :", gpio
