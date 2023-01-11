import ctypes
import sys
import requests
import gc
#GC is a python inbuilt module, that provides an interface to the
#python Garbage collector. It provides features to enable collector,
#disable collector, tune collection frequency, debug options and more.
import numpy as np

'''
x = 10
y = x
  
if id(x) == id(y):
    print("x and y refer to the same object")
else:
    print("x and y are not same object")
#will print that x and y refers to the same object as python optimizes
#memory utilization by allocation the same object reference to a new variable
#if the object already exists with the same value.

'''

'''

a = [12, 2, 5, 6]

print(id(a))

#assigning the memory address of a to x
x = id(a)
print("Memory address - ", x)

#extracting the value from the memory address of a 
b = ctypes.cast(x, ctypes.py_object).value
print("Value - ", b)

'''

'''

c = np.array([1, 2, 3, 4, 5, 6, 7, 34, 56, 78])
  
# get index 4 element address
print("The element present at 4 th  index - element",
      a[4], ":", a[4].data)
print("The size of array is", sys.getsizeof(c), "bytes")

'''
#Memory allocation needs to de-allocated manually in heap memory.
#So when a programmer forgets to clear a memory allocated in heap memory,
#the memory leak occurs. It’s a type of resource leak or wastage.

def call():

	# call the get with a url,here I used google.com
	# get method returns a response object
	response = requests.get('https://google.com')
	
	# print the status code of response
	print("Status code",response.status_code)
	
	# After the function is been returned,
	# the response object becomes non-referenced
	return


def main():
	print("No.of tracked objects before calling get method")
	
	# gc.get_objects() returns list objects been tracked
	# by the collector.
	# print the length of object list with len function.
	print(len( gc.get_objects() ) )
	
	# make a call to the function, that calls get method.
	call()
	
	# collect method immediately free the resource of
	# non-referenced object.
	gc.collect()

	# print the length of object list with len
	# function after removing non-referenced object.
	print("No.of tracked objects after removing non-referenced objects")
	print(len( gc.get_objects() ) )


if __name__ == "__main__":
	main()

