import pyautogui as pg
import time
import keyboard
import win32api
import win32con
# from pyfiglet import Figlet


# while keyboard.is_pressed("q") == False:
#   if keyboard.is_pressed("r"):
#     time.sleep(0.01)
#     pg.click()

# f = Figlet(font='slant')

# print(f.renderText('AutoClicker'))

print('''
      ___         __        _________      __
   /   | __  __/ /_____  / ____/ (_)____/ /_____  _____
  / /| |/ / / / __/ __ \/ /   / / / ___/ //_/ _ \/ ___/
 / ___ / /_/ / /_/ /_/ / /___/ / / /__/ ,< /  __/ /
/_/  |_\__,_/\__/\____/\____/_/_/\___/_/|_|\___/_/

      ''')

def click(duration: float, interval: float):
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(duration)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  time.sleep(interval)

userClickDuration = pg.prompt(text='Click Duration', title='AutoClicker' , default='0.01')
userClickInterval = pg.prompt(text='Interval Between Clicks', title='AutoClicker' , default='0.3')

pg.alert('''
           Auto-Clicker in now running...
           press 'r' to use and 'alt + q' to terminate the program.
           ''', "AutoClicker")

print("AutoClicker Running...")
print("press 'r' to use and 'alt + q' to terminate the program.")


while keyboard.is_pressed("alt+q") == False:
  if keyboard.is_pressed("r"):
    click(duration=float(userClickDuration), interval=float(userClickInterval))