import json

data_log = {'tima': 1234, 'max': 4321}
with open('1.json', 'w') as f:
	json.dump(data_log, f)
log = input('Введите логин:')
passwd = input('Введите пароль:')

def login_function(log, passwd):
	with open('1.json', 'r') as f:
		data_log = json.load(f)
		if log not in data_log.keys():
			print('Повторте попытку!')
		else:
			print('Вход выполнен!')

login_function(log, passwd)