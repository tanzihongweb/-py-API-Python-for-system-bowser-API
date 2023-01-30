import webbrowser
import os,sys,time
import tkinter.messagebox as tm
#Fix bugs must tell maker.
#if you not.Okay fine
def web_create_newtab(url):       #Create a new tab in your default internet bowser
   webbrowser.open_new_tab(url)
def web_show_url(url):
  webbrowser.open(url, new=0, autoraise=True)  #if new=0,in a bowser show.if new=1,not in a bowser!if autoraise is True,forward this window.
def new_bowser_showweb(url):
  webbrowser.open_new(url)
def web_debugging_mode():  #get bowser Information
  webbrowser.get(using=None)
def web_reg(name):
  webbrowser.register(name, constructor, instance=None, *, preferred=False)
#Register the browser type name. Once a browser type is registered, the get() function can return a controller for that browser type. If instance is not provided,
#or is , constructor will be calledwithout parameters to create an instance when needed. If instance is provided, constructor will never be called, and may be .NoneNone
def web_consle():
  webbrowser.name
