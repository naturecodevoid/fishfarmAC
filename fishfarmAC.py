from pynput.mouse import Button, Controller
import keyboard as kb
import time

while True:
	if kb.is_pressed('z'):
		bool = not bool
		time.sleep(0.5)
		ms.click(Button.right, 1)
	if bool == True:
		ms.press(Button.right)
	if kb.is_pressed('f12'):
		break
