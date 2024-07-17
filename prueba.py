def cargar(modelos, cantidades):
    modelo = input('Ingrese el modelo\n').upper()
    while modelo == '' or (modelo != 'FAMILIAR' and modelo != 'UTILITARIO' and modelo != 'FIN'):
        modelo = input('Ingrese nuevamente el modelo\
            n').upper()

    while modelo != 'FIN':
        cantidad = int(input('Ingrese la cantidad:\n'))
        while cantidad <= 0:
            cantidad = int(input('Ingrese la cantidad nuevamente:\n'))

        modelos.append(modelo)
        cantidades.append(cantidad)

        modelo = input('Ingrese el modelo\n').upper()
        while modelo == '' or (modelo != 'FAMILIAR' and modelo != 'UTILITARIO' and modelo != 'FIN'):
            modelo = input('Ingrese nuevamente el modelo\n').upper()

    print(modelos)

def porcentajes(modelos, cantidades):
    cantidades_familiar = 0
    cantidades_utilitario = 0
    cantidad = 0

    for i in range(len(cantidades)):
        cantidad += cantidades[i]

    for i in range(len(modelos)):
        if modelos[i] == 'FAMILIAR':
            cantidades_familiar += cantidades[i]
        else:
            cantidades_utilitario += cantidades[i]

    if cantidades_familiar > 0:
        porcentaje_familiares = (cantidades_familiar * 100) / cantidad
        print(f'El porcentaje de familiares es {porcentaje_familiares} %')
    else:
        print('No se ingresaron modelos Familiares')

    if cantidades_utilitario > 0:
        porcentajes_utilitario = (cantidades_utilitario * 100) / cantidad
        print(f'El porcentaje de utilitarios es {porcentajes_utilitario} %')
    else:
        print('No se ingresaron utilitarios')

def ordenar(modelos, cantidades):
    n = len(modelos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cantidades[j] > cantidades[j + 1]:
                cantidades[j], cantidades[j + 1] = cantidades[j + 1], cantidades[j]
                modelos[j], modelos[j + 1] = modelos[j + 1], modelos[j]

def promedio(modelos, cantidades):
    cant_familiar = 0
    cant_utilitario = 0
    ingresos_familiar = 0
    ingresos_utilitario = 0

    for i in range(len(modelos)):

        if modelos[i]== 'FAMILIAR':
            cant_familiar += cantidades[i]
            ingresos_familiar += 1

        else:
            cant_utilitario += cantidades[i]
            ingresos_utilitario += 1

    promedio_utilitario = cant_utilitario / ingresos_familiar 
    promedio_familiar = cant_familiar / ingresos_utilitario

    print(f'El promedio de modelos familiar es {promedio_familiar}')
    print(f'El promedio de modelos utilitarios {promedio_utilitario}')



def encontrar(modelos, cantidades):
    for i in range(len(modelos)):
        if modelos[i] == 'FAMILIAR':
            if cantidades[i] % 3 == 0:
                modelos[i] = 'Remplazo'
                cantidades[i] = -1

    print(modelos)
    print(cantidades)

def eliminar_datos(modelos, cantidades):
    i = 0
    while i < len(cantidades):
        if cantidades[i] == 7:
            modelos.pop(i)
            cantidades.pop(i)
        else:
            i += 1

    print(modelos)
    print(cantidades)

modelo = []
cantidades = []
cargar(modelo, cantidades)
porcentajes(modelo, cantidades)
ordenar(modelo, cantidades)
promedio(modelo, cantidades)
encontrar(modelo, cantidades)
eliminar_datos(modelo, cantidades)