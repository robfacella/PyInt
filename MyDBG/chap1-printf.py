from ctypes import *

msvcrt = cdll.msvcrt
msg_string = "Hello World!\n"
msvcrt.wprintf("Testing: %s", msg_string)
