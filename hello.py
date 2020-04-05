from __future__ import print_function	# For Py2/3 compatibility
import eel
import random

# Set web files folder
eel.init('web')

@eel.expose
def py_random():
    return random.random()

@eel.expose
def py_list():
    return [1, 2, "3", "4"]

@eel.expose
def py_dict():
    return {
        "1": "hoge",
        "a": "fuga",
    }

class Hoge:
    def __init__(self):
        self.a = "aaaa"
        self.b = "bbbb"
    
    def getA(self):
        return self.a

@eel.expose
def py_class():
    return Hoge()

eel.start('hello.html', size=(400, 300))    # Start
