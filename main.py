
import pyautogui
import time
import datetime
import os
import schedule
import ctypes

global count
count = 0

def hide_console():
    windows = ctypes.windll.kernel32.GetConsoleWindow()
    if windows != 0:
        ctypes.windll.user32.ShowWindow(windows, 0)

def main():
    hide_console()

def take_screenshot():
    global count
    count += 1

    now = datetime.datetime.now()
    file_name = f"screenshot_{now.strftime('%d-%m-%Y_%H-%M-%S')}_{count}.jpeg"
    screenshot = pyautogui.screenshot()
    directory = os.path.join(os.getenv('APPDATA'), 'screenshots', now.strftime('%d-%m-%Y'))

    if not os.path.exists(directory):
        os.makedirs(directory)

    screenshot.save(f"{directory}/{file_name}")

# def main():
#     schedule.every().day.at("00:00").do(take_screenshot)
#     if __name__ == "__main__":
#         schedule.run_pending
#         while True:
#             take_screenshot()
#             time.sleep(30)

if __name__ == "__main__":
    import os

    if os.getenv("CONEMU_PROCESS") == "Y":
        exit()

    schedule.every().day.at("00:00").do(take_screenshot)
    
    hide_console()

    if __name__ == "__main__":
        schedule.run_pending
        while True:
            take_screenshot()
            time.sleep(15)

if __name__ == "__main__":
    main()

