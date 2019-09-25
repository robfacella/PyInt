from ctypes import *

#Windows
msvcrt = cdll.msvcrt
msg_string = "Hello World!\n"
msvcrt.wprintf("Testing: %s", msg_string)

#linux
#libc = cdll("libc.so.6")
#msg_string = "Hello World!\n"
#libc.wprintf("Testing: %s", msg_string)
