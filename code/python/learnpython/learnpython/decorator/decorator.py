'''
 ##################################################################
  Python decorators allow you to change the behavior of a function without modifying the function itself.
###################################################################

# When to Use a Decorator in Python

You'll use a decorator when you need to change the behavior of a function without modifying the function itself. A few good examples are when you want to add logging, test performance, perform caching, verify permissions, and so on.

You can also use one when you need to run the same code on multiple functions. This avoids you writing duplicating code.

To get a better understanding of how decorators work, you should understand a few concepts first.
'''

"""
#####################################################################
1 . A function is an object. Because of that, a function can be assigned to a variable. The function can be accessed from that variable.
####################################################################
"""

def my_function():

    print('I am a function.')

# Assign the function to a variable without parenthesis. We don't want to execute the function.

# description = my_function

# Accessing the function from the variable I assigned it to.

# print(description())

# Output

# 'I am a function.'

"""
######################################################
2.  A function can be nested within another function.
######################################################
"""

def outer_function1():

    def inner_function1():

        print('I came from the inner function.')

    # Executing the inner function inside the outer function.
    inner_function1()


# outer_function1()

# Output

# I came from the inner function


"""
Note that the inner_function is not available outside the outer_function. If I try to execute the inner_function outside of the outer_function I receive a NameError exception.


inner_function()

Traceback (most recent call last):
  File "/tmp/my_script.py", line 9, in <module>
    inner_function()
NameError: name 'inner_function' is not defined
"""

"""
#####################################################################
3.  Since a function can be nested inside another function it can also be returned.
######################################################################
"""

def outer_function2():
    '''Assign task to student'''

    task = 'Read Python book chapter 3.'
    def inner_function2():
        print(task)
    return inner_function2

# homework = outer_function2()
# homework()

# Output

# 'Read Python book chapter 5.'

"""
###############################################################
4.  A function can be passed to another function as an argument.
###############################################################
"""
def friendly_reminder(func):
    '''Reminder for husband'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')
# Calling the friendly_reminder function with the action function used as an argument.

# friendly_reminder(action)

# Output

'''
I am going to the store buy you something nice.
Don't forget to bring your wallet!
'''


"""
#############################################################
How to Create a Python Decorator

To create a decorator function in Python, I create an outer function that takes a function as an argument. There is also an inner function that wraps around the decorated function.
###############################################################

Here is the syntax for a basic Python decorator:
"""
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func




'''
To use a decorator ,you attach it to a function like you see in the code below. We use a decorator by placing the name of the decorator directly above the function we want to use it on. You prefix the decorator function with an @ symbol.
'''

@my_decorator_func
def my_func():

    pass


'''
Here is a simple example. This decorator logs the date and time a function is executed:
'''

from datetime import datetime


def log_datetime(func):
    '''Log the date and time of a function'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

     
# daily_backup()

# Output
'''
Daily backup job has finished.
Function: daily_backup
Run on: 2021-06-06 06:54:14
---------------------------
'''


'''
#################################################################
How to Add Arguments to Decorators in Python

Decorators can have arguments passed to them. To add arguments to decorators I add *args and **kwargs to the inner functions.

    *args  will take an unlimited number of arguments of any type, such as 10, True, or 'Brandon'.
    
    **kwargs will take an unlimited number of keyword arguments, such as count=99, is_authenticated=True, or name='Brandon'.
    
################################################################

Here is a decorator with arguments:
'''

def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Do something before the function.
        func(*args, **kwargs)
        # Do something after the function.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Example docstring for function'''

    pass

'''
Decorators hide the function they are decorating. If I check the __name__ or __doc__ method we get an unexpected result.

'''

# print(my_func.__name__)
# print(my_func.__doc__)

# Output
'''
wrapper_func
None
'''

'''
To fix this issue I will use functools. Functools wraps will update the decorator with the decorated functions attributes.
'''
from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Example docstring for function'''

    pass

'''
Now I receive the output I am expecting.
'''

# print(my_func.__name__)
# print(my_func.__doc__)

# Output
'''
my_func
Example docstring for function
'''
'''
Example of a Python Decorator in Action

I have created a decorator that will measure memory and speed of a function.
We'll use the decorator to test the performance list generation using four methods: range, list comprehension, append, and concatenation.
'''

from functools import wraps
import tracemalloc
from time import perf_counter 


def measure_performance(func):
    '''Measure performance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


# print(make_list1())
# print(make_list2())
# print(make_list3())
# print(make_list4())

# Output
'''
Function: make_list1
Method: Range
Memory usage:		        0.000072 MB 
Peak memory usage:	        3.693040 MB 
Time elapsed is seconds:    0.049359
----------------------------------------

Function: make_list2
Method: List comprehension
Memory usage:		        0.000856 MB 
Peak memory usage:	        3.618244 MB 
Time elapsed is seconds:    0.052338
----------------------------------------

Function: make_list3
Method: Append
Memory usage:		        0.000448 MB 
Peak memory usage:	        3.617692 MB 
Time elapsed is seconds:    0.060719
----------------------------------------

Function: make_list4
Method: Concatenation
Memory usage:		        0.000440 MB 
Peak memory usage:	        4.393292 MB 
Time elapsed is seconds:    61.649138
----------------------------------------
'''

"""
You can use decorators with classes as well. Let's see how you use decorators with a Python class.

In this example, notice there is no @ character involved. With the __call__ method the decorator is executed when an instance of the class is created.

This class keeps track of the number of times a function to query to an API has been run. Once it reaches the limit the decorator stops the function from executing.
"""

import requests


class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return

@LimitQuery
def get_coin_price(limit):
    '''View the Bitcoin Price Index (BPI)'''
    
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


# print(get_coin_price(5))
# print(get_coin_price(5))
# print(get_coin_price(5))
# print(get_coin_price(5))
# print(get_coin_price(5))
# print(get_coin_price(5))

'''
# Output

$35968.25
$35896.55
$34368.14
$35962.27
$34058.26
No queries left. All 5 queries used.
'''

# This class will keep track of the state of the class.

'''
Conclusion

In this article I talked about how to pass a function to a variable, nested functions, returning functions, and passing a function to another function as an argument.

I also showed you how to create and use Python decorators along with a few real-world examples. Now I hope that you will able to add decorators to your projects.

source:
- https://www.freecodecamp.org/news/python-decorators-explained-with-examples/

- https://github.com/brandon-wallace
'''