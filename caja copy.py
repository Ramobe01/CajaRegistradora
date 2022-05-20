#VARIABLES----------------------------------------------------------------------------------------------------------
inventarioAseoHogar = {'BLANQUEADOR':[15300], 'BOLSAS DE BASURA X30':[6000], 'DETERGENTE':[19850], 'JABON REY EN BARRA':[2100], 'LAVALOZA DE LIMON':[2700], 'PAPEL HIGIENICO X12':[17300]}
inventarioAseoPersonal = {'CEPILLO ELECTRICO':[161500], 'CREMA DENTAL':[5300], 'DESODORANTE GILLETE':[17200], 'SHAMPOO':[17850]}
canastaCliente = {}
facturaCliente = 0
tarjetasDebito = {723462:100000,842356:50000,675324:0}

repetirPrincipal = 1
repetirInventario = 1
repetirCategoria = 1
opcionEquivocada = 1
tarjetaEquivocada = 1
numeroInvalido = 1

#FUNCIONES---------------------------------------------------------------------------------------------------------------

#AGREGAR O ELIMINAR MAS PRODUCTOS
def agregarEliminarMasProductos():
    global repetirInventario
    opcionEquivocada = 1
    while opcionEquivocada == 1:
        print("--------------------------------")
        seguirAgregandoProductos = input("1. Agregar o eliminar más productos\n2. Volver al menú principal\nDigite el número de opción a seleccionar: ")
        if(seguirAgregandoProductos == "1"):
            repetirInventario = 1
            opcionEquivocada = 0
        elif(seguirAgregandoProductos == "2"):
            repetirInventario = 0
            opcionEquivocada = 0
        else:
            print("--------------------------------")
            print("Opción incorrecta.\nIntentelo de nuevo.")

#FUNCION AGREGAR PRODUCTOS AL CARRITO
def agregarProductos(categoriaDeProductos):
    global facturaCliente
    for key in sorted(categoriaDeProductos):
        print (key, ':', categoriaDeProductos[key][0],"$")
    print("--------------------------------")
    agregarProducto = input("Digite el nombre del producto que desea añadir a su carrito: ")
    if (agregarProducto.upper() in categoriaDeProductos):
        cantidadProducto = int(input("Digite la cantidad de {0} que desea: ".format(agregarProducto.upper())))
        print("--------------------------------")
        if (cantidadProducto == 1 and agregarProducto.upper() in canastaCliente and type(cantidadProducto) == int):
            print("Se agrego", agregarProducto, "a su carrito")
            canastaCliente[agregarProducto.upper()][1] += cantidadProducto
        elif (cantidadProducto > 1 and agregarProducto.upper() in canastaCliente and type(cantidadProducto) == int):
            print("Se agregaron ({0}) {1} a su carrito".format(cantidadProducto,agregarProducto.upper()))
            canastaCliente[agregarProducto.upper()][1] += cantidadProducto
        elif (not(agregarProducto.upper() in canastaCliente) and cantidadProducto == 1):
            categoriaDeProductos[agregarProducto.upper()].append(1)
            canastaCliente[agregarProducto.upper()] = categoriaDeProductos[agregarProducto.upper()]
            print("Se agrego", agregarProducto, "a su carrito")
        elif (cantidadProducto > 1 and not(agregarProducto.upper() in canastaCliente)):
            categoriaDeProductos[agregarProducto.upper()].append(cantidadProducto)
            canastaCliente[agregarProducto.upper()] = categoriaDeProductos[agregarProducto.upper()]
            print("Se agregaron ({0}) {1} a su carrito".format(cantidadProducto,agregarProducto))
        else:
            print("--------------------------------")
            print("La cantidad de producto debe ser un número y este debe ser mayor que 0")
        facturaCliente += canastaCliente[agregarProducto.upper()][0]*cantidadProducto
        agregarEliminarMasProductos()
    else:
        print("--------------------------------")
        print("Este producto no existe en el inventario, asegurese de digitar el nombre correctamente")

#FUNCION COBRAR DE TARJETA
def cobrarATarjeta():
    global tarjetaEquivocada
    global repetirPrincipal
    global facturaCliente
    print("--------------------------------") 
    comprobarTarjeta = int(input("Inserte el número de su tarjeta de debito: "))
    if(comprobarTarjeta in tarjetasDebito):
        if(tarjetasDebito[comprobarTarjeta] > facturaCliente):
            tarjetasDebito[comprobarTarjeta] -= facturaCliente
            print("--------------------------------") 
            print('La factura ha sido cobrada exitosamente de la tarjeta número',comprobarTarjeta,'El saldo actual es de', tarjetasDebito[comprobarTarjeta], '$')
            tarjetaEquivocada = 0
            facturaCliente = 0
            canastaCliente.clear()
        else:
            print("--------------------------------") 
            print("El saldo es insuficiente")
    else:
        print("--------------------------------")
        print('La tarjeta ',comprobarTarjeta,'no está registrada\nIntentelo de nuevo')

#AÑADIR A INVENTARIO
def añadirAInventario(categoriaAñadirInventario, nombreInventario):
    print("--------------------------------")
    productoAgregar = input("Digite el nombre del producto que desea añadir al inventario {0}: " .format(nombreInventario))
    if(not(productoAgregar.upper() in inventarioAseoHogar or productoAgregar.upper() in inventarioAseoPersonal)):
        precioProducto = input('Inserte el precio de %s: ' % productoAgregar.upper())
        categoriaAñadirInventario[productoAgregar.upper()] = [int(precioProducto)] 
        print("--------------------------------")
        print("Se ha agregado ",productoAgregar.upper()," al inventario {0}".format(nombreInventario))
    else:
        print("--------------------------------")
        print(productoAgregar.upper()," ya se encuentra en el inventario")
#ELIMINAR DEL INVENTARIO
def eliminarDeInventario(categoriaEliminarDeInventario, nombreInventarioEliminar):
    print("--------------------------------")
    for key in sorted(categoriaEliminarDeInventario):
        print (key, ':', categoriaEliminarDeInventario[key][0],"$")
    print("--------------------------------")
    eliminarProducto = input("Digite el nombre del producto que desea eliminar del inventario {0}: " .format(nombreInventarioEliminar))
    if(eliminarProducto.upper() in inventarioAseoHogar or eliminarProducto.upper() in inventarioAseoPersonal):
        del categoriaEliminarDeInventario[eliminarProducto.upper()]
        print("--------------------------------")
        print(eliminarProducto.upper(), "Ha sido eliminado del inventario {0}".format(nombreInventarioEliminar))
    else:
        print("--------------------------------")
        print(eliminarProducto.upper(),"no se encuentra en el inventario")
#MENÚ PRINCIPAL----------------------------------------------------------------------------------------------------------
print("Bienvenido al supermercado sr./sra.\n ¿Qué desea hacer hoy?")
while repetirPrincipal == 1:
    print("--------------------------------")
    menu = print("1. Mostrar inventario\n2. Mostrar carrito \n3. Añadir a cuenta de débito\n4. Retirar de la cuenta de débito\n5. Cobrar\n6. Agregar producto al inventario\n7. Eliminar producto del inventario\n8. Salir")
    opcionPrincipal = input("Escoja el número de opcion a seleccionar: ")

#MENÚ INVENTARIO----------------------------------------------------------------------------------------------------------
    if(opcionPrincipal == "1"):
        repetirInventario = 1
        while repetirInventario == 1:
            print("--------------------------------")
            opcionInventario = input("1. Agregar producto a su carrito \n2. Eliminar producto de su carrito \n3. Atras\nDigite el número de opcion a seleccionar: ")
#AGREGAR PRODUCTOS AL CARRITO----------------------------------------------------------------------------------------------------------
            if (opcionInventario == "1"):
                print("--------------------------------")
                print("Los productos están divididos por categorías\n1. Aseo de Hogar\n2. Aseo Personal")
                opcionCategoria = input("Seleccione la categoría de productos: ")
                print("--------------------------------")
#AGREGAR PRODUCTOS AL CARRITO DE ASEO HOGAR----------------------------------------------------------------------------------------------------------                
                if(opcionCategoria == "1"):
                    agregarProductos(inventarioAseoHogar)
#AGREGAR PRODUCTOS AL CARRITO DE ASEO PERSONAL----------------------------------------------------------------------------------------------------------
                elif(opcionCategoria == "2"):   
                    agregarProductos(inventarioAseoPersonal)                       
#ELIMINAR UN PRODUCTO DEL CARRITO---------------------------------------------------------------------------------------------------------- 
            elif(opcionInventario == "2"):
                print("--------------------------------") 
                print('Su inventario es el siguiente:')
                for inventario in sorted(canastaCliente):
                    print(inventario,'(',canastaCliente[inventario][1],')')
                print("--------------------------------") 
                productoEliminar = input('Ingrese el nombre del producto que desea eliminar: ')
                if(productoEliminar.upper() in canastaCliente):
                    cantidadEliminar = int(input("Digite la cantidad de {0} que desea eliminar: ".format(productoEliminar.upper())))
                    facturaCliente -= canastaCliente[productoEliminar.upper()][0]*cantidadEliminar
                    if(canastaCliente[productoEliminar.upper()][1] > 1 and canastaCliente[productoEliminar.upper()][1] > cantidadEliminar):
                        canastaCliente[productoEliminar.upper()][1] -= cantidadEliminar
                    elif(canastaCliente[productoEliminar.upper()][1] >= 1 and canastaCliente[productoEliminar.upper()][1] <= cantidadEliminar):
                        del canastaCliente[productoEliminar.upper()]
                    print("--------------------------------") 
                    print("(" + str(cantidadEliminar) + ")" + " " + productoEliminar.upper() + " han sido eliminados")
                    
                    agregarEliminarMasProductos()
#-------------------------------------------------------------------------------------------------------------------------------------------
                else:
                    print("--------------------------------")
                    print(productoEliminar,'no se encuentra en su carrito')
#SALIR---------------------------------------------------------------------------------------------------------------------------------------
            else:
                repetirInventario = 0
#MOSTRAR CARRITO----------------------------------------------------------------------------------------------------------    
    elif(opcionPrincipal == "2"):
        tarjetaEquivocada = 1
        while tarjetaEquivocada == 1:
            if (len(canastaCliente) == 0):
                print("--------------------------------")
                print('Su carrito no tiene productos actualmente')
                tarjetaEquivocada = 0
            else:
                print("--------------------------------")
                print('Su carrito tiene: ')
                for i in sorted(canastaCliente):
                    print(i,'(',canastaCliente[i][1],')')
                print('Su factura es actualmente de:' ,facturaCliente,'$')
                cobrarDesdeOpcionCanasta = input("1. Cobrar factura\n2. Volver al menú principal\nDigite el número de opción a seleccionar: ")
                if(cobrarDesdeOpcionCanasta == "1"):
                    cobrarATarjeta()
                elif(cobrarDesdeOpcionCanasta == "2"):
                    tarjetaEquivocada = 0
                    repetirPrincipal = 1
#AÑADIR A CUENTA DE DÉBITO------------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "3"):
        numeroInvalido = 1
        while numeroInvalido == 1:
            print("--------------------------------")
            ingresarTarjeta = int(input("Ingrese el número de la tarjeta: "))
            print("--------------------------------")
            if(ingresarTarjeta in tarjetasDebito):
                saldoIngresar = int(input("Ingrese el valor a depositar: "))
                confirmacion = input("Responder SÍ/NO\n¿Está seguro de que desea ingresar {0} $ a la tarjeta número {1}? " .format(saldoIngresar,ingresarTarjeta))
                if(confirmacion.upper() == "SI" or confirmacion.upper() == "SÍ"):
                    tarjetasDebito[ingresarTarjeta] += saldoIngresar
                    print("--------------------------------")
                    print('El saldo actual es de',tarjetasDebito[ingresarTarjeta],'$')
                    numeroInvalido = 0
                else:
                    numeroInvalido = 0
            else:
                print('La tarjeta',ingresarTarjeta,'no esta registrada')
#RETIRAR DE CUENTA DE DÉBITO----------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "4"):
        numeroInvalido = 1
        while numeroInvalido == 1:
            print("--------------------------------")
            ingresarTarjetaRetirar = int(input("Ingrese el número de la tarjeta: "))
            print("--------------------------------")
            if(ingresarTarjetaRetirar in tarjetasDebito):
                saldoRetirar = int(input("Ingrese el valor a retirar: "))
                if(saldoRetirar <= tarjetasDebito[ingresarTarjetaRetirar]):
                    confirmacionRetiro = input('Responder SÍ/NO\n¿Está seguro de que desea retirar {0} $ de la tarjeta número {1}? '.format(saldoRetirar,ingresarTarjetaRetirar))
                    if(confirmacionRetiro.upper() == "SI" or confirmacionRetiro.upper == "SÍ"):
                        tarjetasDebito[ingresarTarjetaRetirar] -= saldoRetirar
                        print("--------------------------------")
                        print("Fueron retirados {0}$".format(saldoRetirar))
                        print('El saldo actual es de',tarjetasDebito[ingresarTarjetaRetirar],'$')
                        numeroInvalido = 0
                else:
                    print("--------------------------------")
                    print('El saldo actual es de',tarjetasDebito[ingresarTarjetaRetirar],'$')
                    print("El saldo es insuficiente")
                    numeroInvalido = 0
            else:
                print('La tarjeta',ingresarTarjetaRetirar,'no esta registrada')
#COBRAR------------------------------------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "5"):
        tarjetaEquivocada = 1
        while tarjetaEquivocada == 1:
            print("--------------------------------") 
            print('Su factura es actualmente de:' ,facturaCliente,'$')
            cobrarDesdeOpcionCanasta = input("1. Cobrar factura\n2. Volver al menú principal\nDigite el número de opción a seleccionar: ")
            if(cobrarDesdeOpcionCanasta == "1"):
                cobrarATarjeta()
            elif(cobrarDesdeOpcionCanasta == "2"):
                tarjetaEquivocada = 0
                repetirPrincipal = 1
#AGREGAR PRODUCTO AL INVENTARIO------------------------------------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "6"):
        print("--------------------------------")
        print("¿A cúal categoría desea agregar productos?")
        categoriaAñadirInventario = input("1. Aseo Hogar\n2. Aseo Personal\nDigite el número de opción a elegir: ")
#AÑADIR UN PRODUCTO AL INVENTARIO DE ASEO HOGAR-------------------------------------------------------------------------
        if (categoriaAñadirInventario == "1"):
            añadirAInventario(inventarioAseoHogar, "Aseo Hogar")
#AÑADIR UN PRODUCTO AL INVENTARIO DE ASEO PERSONAL-------------------------------------------------------------------------
        elif(categoriaAñadirInventario == "2"):
            añadirAInventario(inventarioAseoPersonal, "Aseo Personal")
#ELIMINAR PRODUCTO DEL INVENTARIO------------------------------------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "7"):
        print("--------------------------------")
        print("¿A cúal categoría desea eliminar productos?")
        categoriaEliminarInventario = input("1. Aseo Hogar\n2. Aseo Personal\nDigite el número de opción a elegir: ")
#ELIMINAR UN PRODUCTO AL INVENTARIO DE ASEO HOGAR-------------------------------------------------------------------------
        if (categoriaEliminarInventario == "1"):
            eliminarDeInventario(inventarioAseoHogar,"Aseo Hogar")

#ELIMINAR UN PRODUCTO AL INVENTARIO DE ASEO PERSONAL-------------------------------------------------------------------------
        elif(categoriaEliminarInventario == "2"):
            eliminarDeInventario(inventarioAseoPersonal,"Aseo Personal")
#SALIR----------------------------------------------------------------------------------------------------------------------------------------
    elif(opcionPrincipal == "8"):
        print("--------------------------------")
        print("¿Está seguro de que desea salir de la registradora?\n1. Sí\n2. No")
        salidaSegura = input("Digite el número de opción a seleccionar: ")
        print("--------------------------------")
        if(salidaSegura.upper() == "1"):
            print("PROGRAMA CERRADO")
            repetirPrincipal = 0
        else:
            repetirPrincipal = 1