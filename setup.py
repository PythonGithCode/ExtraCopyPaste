import keyboard


class settings:
    maxLengthOfCopys = 30

copysOfCtrlC = []

def OnCopyEvent():
    copysOfCtrlC += []


keyboard.add_hotkey('ctrl+c', OnCopyEvent, args=())


# copyShortCut2 = 'ctrl+shift+1'


# keyboard.add_hotkey(copyShortCut2, print, args=())




