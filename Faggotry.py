#!python 2.7.x
import wx

tray_tooltip = 'Faggot Bot'
tray_icon = 'faggot.ico'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetID())
    menu.AppendItem(item)
    return item


class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.set_icon(tray_icon)
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
    
    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Say Hello', self.on_hello)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu
    
    def set_icon(self, path):
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, tray_tooltip)
        
    def set_left_down(self, event):
        print "Tray icon was left-clicked."
        
    def on_hello(self, event):
        print 'Hello, world!'
        
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        
def main():
    app = wx.PySimpleApp()
    TaskBarIcon()
    app.MainLoop()

if __name__ == '__main__':
    main()
