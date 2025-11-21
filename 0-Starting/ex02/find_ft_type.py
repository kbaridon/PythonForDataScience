def all_thing_is_obj(object: any) -> int:
	possibilities = {list: "List", tuple: "Tuple", set: "Set", dict: "Dict"}
	type_obj = type(object)
	if (possibilities.get(type_obj, 0)):
		print(possibilities[type_obj], ":", end=" ")
	elif (type_obj is str):
		print(object, "is in the kitchen :", end=" ")
	else:
		print("Type not found")
		return 42
	print(type(object))
	return 42