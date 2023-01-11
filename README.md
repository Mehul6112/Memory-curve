# Memory-curve

Memory allocation and management is the process of allocating and managing computer memory, which is a valuable resource that 
allows your computer to run programs and perform tasks.
As a Python developer, understanding memory allocation and management is critical for writing efficient and performant code. 
Python, like many programming languages, uses a dynamic memory allocation system, meaning that the Python interpreter automatically 
handles the allocation and deallocation of memory for objects.For example, when working with large data sets, it's often 
necessary to use specific data structures, such as NumPy arrays, that are optimized for memory management, instead of Python's 
built-in lists. Additionally, it's important to be mindful of memory leaks and circular references, which can cause memory to be held 
unnecessarily and lead to performance issues.

Garbage collection: 
  GC is a python inbuilt module, that provides an interface to then python Garbage collector. It provides features to enable collector,
  disable collector, tune collection frequency, debug options and more. It periodically checks for and frees up any memory that is no 
  longer in use by the program, such as objects that are no longer referenced. Additionally, Python has a cyclic garbage collector 
  which specifically deal with cyclic references which can cause memory to be held unnecessarily. 
 
There are two parts of memory:
  1. Stack memory
  2. Heap memory
  
  Stack Memory:
    A stack is a special area of computer’s memory which stores temporary variables created by a function. 
    In stack, variables are declared, stored and initialized during runtime.It is a temporary storage memory. 
    When the computing task is complete, the memory of the variable will be automatically erased.
    
    Advantages:
      
      Helps you to manage the data in a Last In First Out(LIFO) method which is not possible with Linked list and array.
      
      When a function is called the local variables are stored in a stack, and it is automatically destroyed once returned.
      
      A stack is used when a variable is not used outside that function.
      
      It allows you to control how memory is allocated and deallocated.
      
      Stack automatically cleans up the object.
      
      Not easily corrupted.
      
      Variables cannot be resized.
      
    Disadvantages:
      
      Stack memory is very limited.
      
      Creating too many objects on the stack can increase the risk of stack overflow.
      
      Random access is not possible.
      
      Variable storage will be overwritten, which sometimes leads to undefined behavior of the function or program.
      
      The stack will fall outside of the memory area, which might lead to an abnormal termination.
    
  Heap memory:
      The heap is a memory used by programming languages to store global variables. By default, all global 
      variable are stored in heap memory space. It supports Dynamic memory allocation.The heap is not 
      managed automatically for you and is not as tightly managed by the CPU.
      
      Advantages:
      
        Heap helps you to find the greatest and minimum number
        
        Garbage collection runs on the heap memory to free the memory used by the object.
        
        Heap method also used in the Priority Queue.
        
        It allows you to access variables globally.
        
        Heap doesn’t have any limit on memory size.
        
      Disadvantages:
       
        Stack memory is very limited.
        
        Creating too many objects on the stack can increase the risk of stack overflow.
        
        Random access is not possible.
        
        Variable storage will be overwritten, which sometimes leads to undefined behavior of the function or program.
        
        The stack will fall outside of the memory area, which might lead to an abnormal termination.
        
