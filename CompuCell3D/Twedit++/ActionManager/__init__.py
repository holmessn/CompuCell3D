from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qsci import *

from PyQt4 import QtCore, QtGui
import os
import sys
from Messaging import stdMsg, dbgMsg, errMsg, setDebugging

actionDict={}
shortcutToActionDict={}
actionToShortcutDict={}


def addAction(_action):
    name=_action.text()
    name.remove('&')
    # adding only actions with text property set
    if name !='': 
        actionDict[str(name)]=_action
        shortcutText=str(_action.shortcut().toString())
        actionToShortcutDict[str(name)]=shortcutText
        shortcutToActionDict[shortcutText]=str(name)
        

def getAction(_name):
    try:
        return actionDict[_name]
    except KeyError:
        return None

def removeExistingShortcut(_keySequence):
    shortcutText=str(QKeySequence(_keySequence).toString())
    dbgMsg("shortcutText=",shortcutText)
    if str(shortcutText)=='':
        return
    if shortcutText in shortcutToActionDict.keys():
        dbgMsg("FOUND EXISTING SHORTCUT=",shortcutText)
        try:
            actionDict[shortcutToActionDict[shortcutText]].setShortcut('')
            actionToShortcutDict[shortcutToActionDict[shortcutText]]=''
                
            del shortcutToActionDict[shortcutText]
            dbgMsg("Removing shortcutText=",shortcutText)
        except KeyError:
            
            pass


def setActionKeyboardShortcut(_name,_keySequence):        
    try:        
        dbgMsg("BEFORE actionToShortcutDict=",len(actionToShortcutDict))
        dbgMsg("_name=",_name," sequence=",_keySequence.toString())
        
        shortcutText=str(QKeySequence(_keySequence).toString())
        
        removeExistingShortcut(shortcutText)
        
        # remove shortcut for the action for which we are doing reassignment
        removeExistingShortcut(actionToShortcutDict[str(_name)])
        actionDict[str(_name)].setShortcut(QKeySequence(shortcutText))        
        dbgMsg("_name=",_name)
        dbgMsg("before assign actionToShortcutDict=",len(actionToShortcutDict))
        actionToShortcutDict[str(_name)]=shortcutText
        shortcutToActionDict[shortcutText]=str(_name)
        dbgMsg("actionToShortcutDict=",len(actionToShortcutDict))
        dbgMsg("shortcutToActionDict=",len(shortcutToActionDict))
        dbgMsg("actionDict=",len(actionDict))
        
        
    except KeyError:
        dbgMsg("KeyError setActionKeyboardShortcut(")
        return None
        
def getActionKeyboardShortcut(_name):        
    try:
        return actionDict[str(_name)].shortcut().toString()
    except KeyError:
        return None
    