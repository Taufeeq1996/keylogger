from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlMouse():
    mouse = Controller()
    #(left to right, top to bottom) in pixels
    mouse.position = (100, 20)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type('Surprise Surprise')

controlKeyboard()


# controlMouse()
# controlling your mouse
# listening to your mouse
# controlling your keyboard
# listening to your keyboard -- will be finally used in our keylogger