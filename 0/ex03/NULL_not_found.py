"""
EXPECTED OUTPUT:
$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
Cheese: nan <class 'float'>$
Zero: 0 <class 'int'>$
Empty: <class 'str'>$
Fake: False <class 'bool'>$
Type not Found$
1$
$>
"""
def NULL_not_found(object: any) -> int:
	obj_type = type(object)

	name = ""

	if (str(object) == "nan" and obj_type != str):
		name = "Cheese"
	elif (obj_type.__name__ == "NoneType"):
		name = "Nothing"
	elif obj_type == int and object == 0:
		name = "Zero"
	elif obj_type == str and object == "":
		name = "Empty"
	elif obj_type == bool and object == False:
		name = "Fake"
	else:
		print("Type not found")
		return 1

	print(f'{name}: {object} {obj_type}')

	return 1
