import  win32file
import  win32api

drivers=win32api.GetLogicalDriveStrings().split('\0')
for drive in drivers[:]:
	print drive
	if win32file.GetDriveType(drive) != win32file.DRIVE_REMOVABLE:
        	drivers.remove(drive)
		print drive