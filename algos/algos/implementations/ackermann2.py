# Configuration

PARAM_1 = 2  			# Ackermann(PARAM_1, PARAM_2)
PARAM_2 = 1  			# ...

PRINT_STEPS = True		# print mathematical form of each step
PRINT_VARS = False		# print x, y, and x_list values for each step
PRINT_X_LIST = False  	# print all recorded x-values for each step


def A(x, y, x_list=[]):
	""" Ackermann function with step printing and two other additional options.
	Brief:
		The actual Ackermann portion of this code is very short:
			def A(x, y):
				if x == 0:
					y = y + 1
				elif y == 0:
					y = A(x - 1, 1)
				else:
					y = A(x - 1, A(x, y - 1))
				return y
		It's the tracking and printing of each step that makes the code larger.
	Args:
		x (int): The first parameter in the Ackermann function.
		y (int): The second parameter in the Ackermann function.
		x_list (list): The list in which x-values are recorded, as needed for
			printing each step in mathematical form. This parameter should not
			be set when calling the function.
	Returns:
		int: Result of the Ackermann function, which is the final y-value.
	"""
	# keep track of x_list length to prevent unexpected deletion of x-values
	length = len(x_list)
	# add current x-value to the list
	x_list.append(x)
	# invoke additional options based on config variables, such as printing
	# each step in mathematical form, printing all values, or printing x_list
	additional_options(x, y, x_list)
	# Ackermann
	if x == 0:
		y = y + 1;
		# if the last recorded x-value is 0, delete it -- it's done its job
		if x_list and x_list[-1] == 0: 
			del x_list[-1]
	elif y == 0:
		# delete the last recorded x-value; expecting a new one in its place
		del x_list[-1]
		# Ackermann
		y = A(x - 1, 1)
		# on return from recursion, if last recorded x-value is 0, delete it
		if x_list and x_list[-1] == 0: 
			del x_list[-1]
	else:
		# update the last recorded x-value (decrement by 1)
		del x_list[-1]
		x_list.append(x - 1)
		# Ackermann (x > 0, y > 0)
		y = A(x - 1, A(x, y - 1))
		# when the program returns back to this state, decide whether the last
		# x-value in the x_list should be removed
		if x_list and x_list[-1] <= x and length == len(x_list): 
			del x_list[-1]
	return y


# invokes additional options based on the configuration variables
def additional_options(x, y, x_list):
	# print current step of the computation
	if PRINT_STEPS:
		print_step(x_list, y)
	# print current values of x, y, and x_list size
	if PRINT_VARS:
		print_variables(x, y, len(x_list))
	# print all the stored x-values for this step
	if PRINT_X_LIST:
		print_list(x_list)


# prints the current step of the calculation in mathematical form, like:
# A(2, A(1, A(2, 0)))
def print_step(x_list, y):
	for i in range(len(x_list)):
		print("A(" + str(x_list[i]) + ", ", end="")
	print(str(y) + ")" * len(x_list))


# prints x, y, and x_list size values for the current state, in this format:
# x = 2		y = 1	depth = 1
def print_variables(x, y, x_list_size):
	print("x = " + str(x) + 
		  "\t y = " + str(y) + 
		  "\t depth = " + str(x_list_size))


# prints all current records of x-values
def print_list(x_list):
	print(x_list)


def main():
	# invoke the Ackermann function and print its final result
	print(A(PARAM_1, PARAM_2))

