import json
log = int (input('Введите логин:'))
passwd = int(input('Введите пароль:'))
data = {}
def register(log, passwd):
	if log not in data.keys():
		data[log] = passwd
		with open('1.json', 'w') as f:
			json.dump(data, f)

register(log, passwd)
print ('Данные успешно приняты!')