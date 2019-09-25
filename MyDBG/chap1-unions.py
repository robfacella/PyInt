from ctypes import *

#Windows
class barley_amount(Union):
    _fields_ = [
    ("barley_long", c_long),
    ("barley_int", c_int),
    ("barley_char", c_char),
    ]

value = input("Enter the amount of barley to throw in the beer vat: ")
my_barley = barley_amount(int(value))
print ("Barley amount as a long: %ld" % my_barley.barley_long)
print ("Barley amount as an int: %d" % my_barley.barley_int)
print ("Barley amount as an ASCII char: %s" % my_barley.barley_char)
