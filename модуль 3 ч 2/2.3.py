d = {"name1": "idi1", "name2": "idi2", "name3": "idi3"}
print (d)
d2 = {
	value: key
	for key, value
	in d.items()
}
print(d2)