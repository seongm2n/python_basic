import sys
import inspect
# from ..sub1 import module1

# module3.py
def mod3_test1():
	print ("Module3 -> Test1")
	print("Path : ", inspect.getfile(inspect.currentframe()))

def mod3_test2():
	print ("Module3 -> Test2")
	print("Path : ", inspect.getfile(inspect.currentframe()))
