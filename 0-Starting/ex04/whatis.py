import sys

if (len(sys.argv) == 1):
	sys.exit()
if (len(sys.argv) > 2):
	raise AssertionError("more than one argument is provided")
try:
	n = int(sys.argv[1])
	if (n % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
except ValueError:
	raise AssertionError("argument is not an integer") from None