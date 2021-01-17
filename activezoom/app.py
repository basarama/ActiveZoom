import sys
import time
import win32gui
import ctypes

import random
import activezoom.notification

def callback(hwnd, strings):
    if win32gui.IsWindowVisible(hwnd):
        window_title = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if window_title and right-left and bottom-top:
            strings.append('0x{:08x}: "{}"'.format(hwnd, window_title))
    return True

def run():
    in_zoom = False
    been_notified = True

    while(not time.sleep(5)):
        win_list = []  # list of strings containing win handles and window titles
        win32gui.EnumWindows(callback, win_list)  # populate list
        print()
        in_zoom = False
        for window in win_list:  # print results
            if("Zoom Meeting" in window):
                print(window)
                in_zoom = True
                been_notified = False
        
        if (not in_zoom and not been_notified):
            activezoom.notification.display_popup("Zoom Meeting Ended\n You should work out!")
            been_notified = True

"""
# Todo
- Request user to run program at startup
- Fix random picking non-existant exercise
- Update RNG to favour new exercises
- Get user feedback to increase difficulty or opt out of exercises
- Add ML
- save settings
"""