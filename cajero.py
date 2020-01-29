print('\n                         Bienvenido al cajero Idat \n')

opciones = ['Crear cuenta bancaria', 'Consultar cuenta', 'Retirar dinero', 'Depositar dinero']
opcion_verificada = False
cuentas = [[1995, 'Erick', '123', 500.00], [1996, 'Other user', '123', 500.00]]

# Este es un valor que cambiará solo cuando se cree una nueva cuenta
nro_cuenta_por_defecto = 1995


# Funciones

#Mostrar opciones
def mostrarOpciones():
	# Imprimir opciones
	print('\nOpciones\n')
	for opcion in opciones:
		print(f"{opciones.index(opcion)}- {opcion}")

# Verificar si la opción existe
def verificarOpcion():
	for opcion in opciones:
		if opciones.index(opcion) == opcion_seleccionada:
			opcion_verificada = True
			return opcion_verificada

def dirigirAOpciones():
	# Imprimir opciones
	opcion_verificada = False
	mostrarOpciones()
	opcion_seleccionada = int(input('\nIngrese el número de la opción: '))
	opcion_verificada = verificarOpcion()

	if opcion_verificada:
		if opcion_seleccionada == 0:
			crearCuenta()
		elif opcion_seleccionada == 1:
			consultarCuenta()
		elif opcion_seleccionada == 2:
			retirarDinero()
		elif opcion_seleccionada == 3:
			depositarDinero()

def consultarCuenta():
	print('\n                         Estás consultando tú cuenta')
	nro_cuenta_a_consultar = int(input('\nIngrese el número de cuenta a consultar o \ningresa 1 para regresar al menú principal: '))
	nro_cuenta_validado = False

	if(nro_cuenta_a_consultar == 1):
		dirigirAOpciones()
	else:
		for cuenta in cuentas:
			if nro_cuenta_a_consultar in cuenta:
				nro_cuenta_validado = True
				break
			else:
				nro_cuenta_validado = False
				continue

		# Mostrar datos de la cuenta
		if cuentas:
			if nro_cuenta_validado:
				print('\n Datos de la cuenta: \n')
				print(f'Número de cuenta: {cuenta[0]}')
				print(f'Nombre del cliente: {cuenta[1]}')
				print(f'Dinero disponible: {cuenta[3]}\n')
				dirigirAOpciones()
			else:
				print('\nEl número de cuenta es incorrecto, inténtalo nuevamente. \n')
				consultarCuenta()
		else:
			print('\nNo existen cuentas, puedes crear una ahora.\n')
			dirigirAOpciones()

# Crear cuenta
def crearCuenta():
	# Obtenemos la variable global para modificarla
	global nro_cuenta_por_defecto

	# Crear cuenta bancaria
	print('\n                         Está creando una nueva cuenta \n')

	nueva_cuenta = []
	print(f'\nSe generó un número de cuenta automáticamente: {nro_cuenta_por_defecto} \n')

	nombre = input('Ingrese su nombre: ')
	clave = input('Ingrese su clave: ')
	monto = 0.00


	# Añadimos valores a nueva cuenta
	nueva_cuenta.append(nro_cuenta_por_defecto)
	nueva_cuenta.append(nombre)
	nueva_cuenta.append(clave)
	nueva_cuenta.append(monto)

	print('\n************ Tú cuenta fue creada satisfactoriamente ************\n')

	# Sumamos 1 a número de cuenta, para que al crear otra cuenta, no tengan el mismo número
	nro_cuenta_por_defecto += 1

	# Añadimos una cuenta a las lista de cuentas
	cuentas.append(nueva_cuenta)

	# Regresamos el valor de opción seleccionada a False para que el usuario pueda elegir nuevamente
	opcion_verificada = False

	dirigirAOpciones()

# Retirar dinero
def retirarDinero():
	print('\n                         Estás retirando dinero de tú cuenta')
	nro_cuenta_a_retirar = int(input('\nIngrese su número de cuenta o \ningresa 1 para regresar al menú principal: '))
	nro_cuenta_validado = False

	if(nro_cuenta_a_retirar == 1):
		dirigirAOpciones()
	else:
		for cuenta in cuentas:
			if nro_cuenta_a_retirar in cuenta:
				nro_cuenta_validado = True
				break
			else:
				nro_cuenta_validado = False
				continue

	if nro_cuenta_validado:
		monto_a_retirar = float(input('Ingrese el monto a retirar: '))
		monto_actual = cuenta[3]
		if(monto_actual < monto_a_retirar):
			print('\n No cuentas con suficiente dinero.')
			dirigirAOpciones()
		else:
			monto_final = monto_actual - monto_a_retirar

			# Asignar nuevo valor a cuenta
			cuenta[3] = monto_final
			print('\nEl monto fue retirado.')
			dirigirAOpciones()
	else:
		print('\nEl número de cuenta es incorrecto, inténtalo nuevamente. \n')
		retirarDinero()

# Depositar dinero
def depositarDinero():
	print('\n                         Estás depositando dinero a tú cuenta')
	nro_cuenta_a_depositar = int(input('\nIngrese su número de cuenta o \ningresa 1 para regresar al menú principal: '))
	nro_cuenta_validado = False

	if(nro_cuenta_a_depositar == 1):
		dirigirAOpciones()
	else:
		for cuenta in cuentas:
			if nro_cuenta_a_depositar in cuenta:
				nro_cuenta_validado = True
				break
			else:
				nro_cuenta_validado = False
				continue

	if nro_cuenta_validado:
		monto_a_depositar = float(input('Ingrese el monto a depositar: '))
		monto_actual = cuenta[3]

		# Añadir dinero
		monto_final = monto_actual + monto_a_depositar

		# Asignar nuevo valor a cuenta
		cuenta[3] = monto_final

		print('\nEl monto fue depositado a tú cuenta.')
		dirigirAOpciones()
	else:
		print('\nEl número de cuenta es incorrecto, inténtalo nuevamente. \n')
		depositarDinero()

# Aquí empieza el programa
mostrarOpciones()
opcion_seleccionada = int(input('\nIngrese el número de la opción: '))

if opcion_seleccionada == 0:
	crearCuenta()
elif opcion_seleccionada == 1:
	consultarCuenta()
elif opcion_seleccionada == 2:
	retirarDinero()
elif opcion_seleccionada == 3:
	depositarDinero()