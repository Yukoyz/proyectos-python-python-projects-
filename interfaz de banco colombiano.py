while True: #Bucle infinito para mostrar el menú de opciones hasta que el usuario decida salir

    print('Bienvenido')

    #lista de opciones
    print('Seleccione una de las opciones')
    print('1.Enviar dinero')
    print('2.Ver el precio del dolar')
    print('Salir')
    
    opcion= (input('Seleccione la opcion: '))

    if opcion == '1': #Opción para enviar dinero a otra persona
        print('el numero debe de tener 10 digitos')
        try: #Manejo de errores para evitar que el programa se caiga si el usuario ingresa un valor no numérico
            num_cuenta = float(input('ingrese el numero de cuenta de la persona a la que va a transferir el dinero: '))
            num1_monto = float(input('monto del dinero: '))
            print('dinero enviado con exito\n')
        except ValueError: #Manejo de errores para evitar que el programa se caiga si el usuario ingresa un valor no numérico
            print('Error: Por favor, ingrese un número válido.\n')



    elif opcion == '2': #Opción para ver el precio del dólar
        try: 
            print('el precio del dolar es de 3660')
            cantidad_pesos = float(input('¿Cuántos pesos quieres convertir a dólares?: '))
            precio_dolar = 3660
            resultado = (cantidad_pesos/precio_dolar)
            print(f'el valor del peso colombiano a dolares es: {resultado} USD\n') #aquí se muestra el resultado de la conversión de pesos a dólares
        except ValueError:
            print('Error: Por favor, ingrese un número válido.\n')

    elif opcion == '3' or opcion.lower() == 'salir':
        break #Opción para salir del programa, se rompe el bucle infinito y se termina la ejecución del programa

