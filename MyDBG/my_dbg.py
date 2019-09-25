from ctypes import *
from my_dbg_defines import *

kernel32 = windll.kernel32

class debugger():
    def _init_(self):
        pass

    def load(self, path_to_exe):
        #dwCreation flag determines how to create the process
        #To see the GUI for the process
        #creation_flags = CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS

        #instantiate structures
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        #The following 2 options allow the started process to be shown as a separate window.
        #It also illustrates how different settings in the STARTUPINFO struct can affect the Debugger
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        #Then initialize the cb var in the STARTUPINFO struct which is the size of the struct itself
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessA(path_to_exe,
                                None,
                                None,
                                None,
                                None,
                                creation_flags,
                                None,
                                None,
                                byref(startupinfo),
                                byref(process_information)):
            print("[*] We have successfully launched the process!")
            print("[*] PID: %d" % process_information.dwProcessId)
        else:
            print("[*] ERROR: 0x%08x." % kernel32.GetLastError())
