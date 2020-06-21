## Script made by KanuX for Fish Farm tutorial ##
## Follow me: twitch.tv/kanux14 ##

from pynput.mouse import Button, Controller
import keyboard as kb
import time

wait = time.sleep
ms = Controller()
bool = False

while True:
	if kb.is_pressed('z'):
		bool = not bool
		wait(0.5)
		ms.click(Button.right, 1)
	if bool == True:
		ms.press(Button.right)
	if kb.is_pressed('f12'):
		break
