"""
Lihat source code di folder code/python/learnpython/learnpython/decorator.py
"""


from learnpython import decorator

# 1. fungsi adalah sebuah sebuah object,oleh karena itu fungsi dapat diassign ke variable
description = decorator.my_function

# 2 sebuah fungsi bisa bersarang di fungsi yang lain
outer = decorator.outer_function1
"""
catatan:
	- inner_function1 tidak bisa dikenali diluar scope outer_function1
"""
# try:
# 	decorator.inner_function1()
# except Exception as e:
# 	print(e)
# 	# lihat traceback
# 	print("lihat inner_function1 tidak bisa dieksekusi")

# 3 karena sebuah fungsi dapat bersarang di fungsi yang lain maka ia juga bisa menjadi sebuah return fungsi
homework = decorator.outer_function2()


# 4 sebuah fungsi dapat dipassing sebagai argument di fungsi yang lain
remainder = decorator.friendly_reminder
action	  = decorator.action

# membuat decorator
backup = decorator.daily_backup


if __name__ == "__main__":
	# 1
	print(description())

	# 2
	outer()

	# 3 
	homework()
	
	# 4
	remainder(action)

	# print decorator backup
	backup()