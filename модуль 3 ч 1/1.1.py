x = float(input('Введите сумму вкладав в рублях:'))
p = float(input('Введите процент:'))
y = float(input('Введите желаемую итоговую сумму:'))
z = (x//100)*p 
n = (y - x) // z
round (n)
print('Итоговая сумма будет доступна через:' , n ,'лет(годa)')