import math

def NULL_not_found(object: any) -> int:
	possibilities = {None: "Nothing:", '0': "Zero:", "": "Empty:", False: "Fake:"}
	if (type(object) is float and math.isnan(object)):
		print("Cheese:", object, type(object))
		return (0)
	if (not possibilities.get(object, "")):
		print("Type not Found")
		return (1)
	if (type(object) is int):
		print("Zero:", object, type(object))
	else:
		print(possibilities[object], object, type(object))
	return (0)