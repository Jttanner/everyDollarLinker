import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(pyautogui.pixel(x, y))
except KeyboardInterrupt:
    print('\n')