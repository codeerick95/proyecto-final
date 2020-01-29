cuentas = [[1995, 'Erick', '123', 0], [1996, 'E', '123', 10]]
nro_cuenta = int(input('Número de cuenta '))

for cuenta in cuentas:
	existe = nro_cuenta in cuenta
	if existe:
		print('existe')
	else:
		print('No existe')