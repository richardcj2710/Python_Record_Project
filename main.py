import pyautogui
import keyboard
import os 
from PIL import Image, ImageSequence
from datetime import datetime

frame = []
exit_program = False

def on_hotkey(event):
  global exit_program
  if event.name == 'esc' and keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt'):
    print("Exiting...")
    exit_program = True
    
keyboard.on_press(on_hotkey)

while not exit_program:
  img = pyautogui.screenshot()
  img = img.convert("RGB")
  frames.append(img)

current_time = datetime.now(),strftime("%d-%m-%y")

floder_path = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(folder_path, "GIFs")
os.makedirs(folder_path, exist_ok = True)

file_name = f"{folder_path}/record_{current_time}.gif"

frames[0].save(file_name, save_all = True, append_images = frame[1:], loop = 0, duration = 200)
