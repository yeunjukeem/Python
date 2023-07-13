#func_import.py

import func_kwargs
from func_args import 함수
from func_kwargs import *

from func_kwargs import name_hello_함수 as nh
import numpy as np

#
#
#

#func_kwargs.name_hello_함수(a= "kim", b = "park", c = "lee")
nh(a=)





#상위경로 import

import sys, os
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
print(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import hello

file_path= "C:\apps\test"
sys.path.append(file_path)


list_1 = [1,2,3,4,5]
list_2 = []

a = np.array(list_1)
b = np.array(list_2)
print(list_1 + list_2)

###



