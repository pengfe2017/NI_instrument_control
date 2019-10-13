# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:50:07 2019

this referenced to: 
https://forums.ni.com/t5/PXI/
Recommended-approach-for-PXI-control-from-Python/td-p/3679439?profile.language=zh-CN

@author: 李鹏飞
"""

from ctypes import c_bool, c_int, c_double, c_char_p, byref, windll

NIDCPOWER_VAL_DC_VOLTAGE = 1006

def c_string(s):
  return c_char_p(str(s).encode('utf-8'))

dll = windll.LoadLibrary('nidcpower_64.dll')
vi = c_int(0) # vi "declared" here to be set by reference in next line
dll.niDCPower_InitializeWithChannels(c_string('PXI1Slot6'), c_string('0'), c_bool(True), c_string(''), byref(vi)) # Module name PXIxSloty will depend on your setup!
dll.niDCPower_ConfigureOutputFunction(vi, c_string('0'), c_int(NIDCPOWER_VAL_DC_VOLTAGE))
dll.niDCPower_ConfigureVoltageLevel(vi, c_string('0'), c_double(3.3)) # Set output to 3.3V
dll.niDCPower_Initiate(vi)
dll.niDCPower_ConfigureOutputEnabled(vi, c_string('0'), c_bool(True))


#%% some update

from ctypes import c_bool, c_int, c_double, c_char_p, byref, windll, cdll
from ctypes.util import find_library

def c_string(s):
        return c_char_p(str(s).encode('utf-8'))
lib_name = find_library('nidcpower_32')
dll = cdll.LoadLibrary(lib_name)

#%% working scripts

from ctypes import c_bool, c_int, c_double, c_char_p, byref, windll, cdll
from ctypes.util import find_library
import time

def c_string(s):
        return c_char_p(str(s).encode('utf-8'))

lib_name = find_library('nidcpower_32')
dll = windll.LoadLibrary(lib_name)#C:\Program Files\IVI Foundation\IVI\Bin\nidcpower_32.dll
vi = c_int(0)
dll.niDCPower_InitializeWithChannels(c_string('PXI1Slot7'), c_string('0'), c_bool(True), c_string(''), byref(vi))
dll.niDCPower_ConfigureOutputFunction(vi, c_string('0'), c_int(1006))
dll.niDCPower_ConfigureVoltageLevel(vi, c_string('0'),c_double(3.1))
dll.niDCPower_Initiate(vi)
dll.niDCPower_ConfigureOutputEnabled(vi, c_string('0'), c_bool(True))