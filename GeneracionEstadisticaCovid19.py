import random

#validacion de numero ingresado
def esPositivo(n):
    while n < 0:
        print('El numero debe ser mayor o igual a cero: ')
        n = int(input('Ingrese nuevamente: '))
    
    return n

#Funciones que generan resultados aleatorios
def edad():
    edad = random.randint(1,110)
    return edad

def resultadoTest():
    valores = 'Positivo', 'Negativo'
    resultado = random.choice(valores)
    return resultado

def contactoCasos():
    valores = True, False
    contacto = random.choice(valores)
    return contacto

def region():
    valores = 'Capital', 'Gran Cordoba', 'Norte', 'Sur'
    region = random.choice(valores)
    return region

def viajeExterior():
    valores = True, False
    viajo = random.choice(valores)
    return viajo

def personalSalud():
    valores = True, False
    personal = random.choice(valores)
    return personal

#Test
def test():

    print('=' * 80)
    print('PROGRAMA PARA GENERACION DE ESTADISTICA DE COVID-19')
    print('=' * 80)
    print()

    usuario_ok = False
    intentos = 0
    while usuario_ok != True and intentos < 3:
        
        usuario = input('ingrese el usuario (solo tiene 3 intentos): ')
        intentos += 1

        while len(usuario) < 7:
            usuario_ok = False
            break
        
        contCaracteres = 0
        contArrobas = 0
        caracterAnterior = None
        arroba_ok = False
        punto_ok = False
        for i in usuario:
            contCaracteres += 1
            
            if i == ' ':
                usuario_ok = False
                break
            if i == '@':
                contArrobas += 1
                if contArrobas > 1:
                    arroba_ok = False
                    break
                # el carater "@" tiene que estar entre la posicion 2 y la total -4 (tomando en cuenta el ".com")
                if contCaracteres > 1 and contCaracteres < (len(usuario)-4):
                    arroba_ok = True
                else:
                    arroba_ok = False
                    usuario_ok = False
                    break
            
            if i == '.':
                if caracterAnterior == '.':
                    punto_ok = False
                    break
                if contCaracteres == 1 or contCaracteres == len(usuario):
                    punto_ok = False
                    break
                else:
                    punto_ok = True
            
            caracterAnterior = i
        
        
        if arroba_ok and punto_ok:
            usuario_ok = True
            print('USUARIO CORRECTO')
            print()
            break
        else:
            if intentos == 3:
                print('Ha excedido la cantidad de intentos.. PROGRAMA FINALIZADO')                
                exit()
            else:
                print('Hubo un erro en la validacion')
                print()
                usuario_ok = False

        
    cantPacientes = esPositivo(int(input('Ingrese la cantidad de pacientes a procesar: ')))

    contadorCasosPositivos = acumuladorEdadPacientesRiesgo = contadorPersonalSalud = acumuladorEdad = confirmadosCapital = 0
    confirmadosGranCordoba = confirmadosNorte = confirmadosSur = confirmadosConViaje = sospechososContactoConfirmados = 0
    cantidadPacientesRiesgo = menorEdad = contadorCasosAutoctonos = 0

    for i in range(cantPacientes):
        paciente = edad(), resultadoTest(), contactoCasos(), region(), viajeExterior(), personalSalud()
        
        #cantidad de casos confirmados
        if paciente[1] == 'Positivo':
            contadorCasosPositivos += 1
            acumuladorEdad += paciente[0]

            #cantidad de casos por region 
            if paciente[3] == 'Capital':
                confirmadosCapital += 1
            elif paciente[3] == 'Gran Cordoba':
                confirmadosGranCordoba += 1
            elif paciente[3] == 'Norte':
                confirmadosNorte += 1
            else:
                confirmadosSur += 1

            #contidad de casos con viaje al exterior
            if paciente[4] == True:
                confirmadosConViaje += 1

            #cantidad de confirmados en contacto con sospechosos
            if paciente[2] == True:
                sospechososContactoConfirmados += 1
            
            #Menor edad entre casos autoctonos
            if paciente[2] == False and paciente[5] == False and paciente[4] == False:
                contadorCasosAutoctonos += 1 
                if i == 0:
                    menorEdad = paciente[0]
                else:
                    if menorEdad < paciente[0]:
                        menorEdad = paciente[0]
            
            #Personal de salud
            if paciente[5] == True:
                contadorPersonalSalud += 1

        #Pacientes de riesgo
        if paciente[0] > 60 and paciente[1] == 'Negativo':    
            acumuladorEdadPacientesRiesgo += paciente[0]
            cantidadPacientesRiesgo += 1
        
        
    #Menu de opciones y solucion.
    opcion = -1

    while opcion != 0:
        print()
        print('Ingrese\n'
        '1. Cantidad de casos confirmados y porcentaje sobre total de casos\n'
        '2. Edad promedio de pacientes que pertenecen a grupos de riesgo\n'
        '3. Cantidad y porcentaje que el personal de salud representa sobre el total de casos\n'
        '4. Edad Promedio entre los casos confirmados\n'
        '5. Menor edad entre los casos autoctonos\n'
        '6. Cantidad de casos confirmados por region y porcentaje de cada region sobre el total\n'
        '7. Cantidad de casos confirmados con viaje al exterior\n'
        '8. Cantidad de casos sospechosos en contacto con casos confirmados\n'
        '9. Regiones sin casos confirmados\n'
        '10. Porcentaje de casos positivos autoctonos sobre el total de positivos\n'
        '0. SALIR')
        opcion = int(input('Opcion: '))

        if opcion == 1:
            porcent_confirmadosSobreTotal = (contadorCasosPositivos * 100)/cantPacientes

            print('Cantidad de casos confirmados: ', contadorCasosPositivos)
            print('Porcentaje sobre el total de casos: ', round(porcent_confirmadosSobreTotal, 2),'%')

        elif opcion == 2:
            promedioEdadPaciRiesg = acumuladorEdadPacientesRiesgo / cantidadPacientesRiesgo

            print('La edad promedio de los pacientes que pertenecen a un grupo de riesgo es de: ', round(promedioEdadPaciRiesg), 'años.')
        
        elif opcion == 3:
            porcent_persSaludSobreTotal = (contadorPersonalSalud * 100) / cantPacientes

            print('Cantidad de casos de personal de salud: ', contadorPersonalSalud)
            print('Porcentaje sobre el total de casos: ', round(porcent_persSaludSobreTotal, 2), '%')
        
        elif opcion == 4:
            promedioEdadSobreConfirmados = acumuladorEdad / contadorCasosPositivos

            print('La edad promedio entre los casos confirmados es de: ', round(promedioEdadSobreConfirmados), 'años')
        
        elif opcion == 5:
            if menorEdad == 0:
                print('No hubo casos autoctonos')
            else:            
                print('La menor edad entre los casos autoctonos es de: ', menorEdad, 'años')
        
        elif opcion == 6:
            #Capital
            porcen_capitalSobreTotal = (confirmadosCapital * 100) / contadorCasosPositivos

            print('Cantidad de casos confirmados en Capital: ', confirmadosCapital)
            print('Porcentaje que representa sobre el total de casos: ', round(porcen_capitalSobreTotal, 2), '%')

            #Gran Cordoba
            porcen_GranCordobaSobreTotal = (confirmadosGranCordoba * 100) / contadorCasosPositivos

            print('Cantidad de casos confirmados en Gran Cordoba: ', confirmadosGranCordoba)
            print('Porcentaje que representa sobre el total de casos: ', round(porcen_GranCordobaSobreTotal, 2), '%')

            #Norte
            porcen_NorteSobreTotal = (confirmadosNorte * 100) / contadorCasosPositivos

            print('Cantidad de casos confirmados en Norte: ', confirmadosNorte)
            print('Porcentaje que representa sobre el total de casos: ', round(porcen_NorteSobreTotal, 2), '%')

            #Sur
            porcen_SurSobreTotal = (confirmadosSur * 100) / contadorCasosPositivos

            print('Cantidad de casos confirmados en Sur: ', confirmadosSur)
            print('Porcentaje que representa sobre el total de casos: ', round(porcen_SurSobreTotal, 2), '%')
        
        elif opcion  == 7:
            print('La cantidad de casos confirmados con viaje al exterior es de: ', confirmadosConViaje, ' Personas')
        
        elif opcion == 8:
            print('La cantidad de casos sospechosos que estuvieron en contacto con casos confirmados es de: ', sospechososContactoConfirmados, ' Personas')
        
        elif opcion == 9:
            if confirmadosCapital == 0:
                print('No hubo casos confirmados en Capital')
            if confirmadosGranCordoba == 0:
                print('No hubo casos confirmados en Gran cordoba')
            if confirmadosNorte == 0:
                print('No hubo casos confirmados en Norte')
            if confirmadosSur == 0:
                print('No hubo casos confirmados en Sur')
            
            if confirmadosCapital != 0 and confirmadosGranCordoba != 0 and confirmadosNorte != 0 and confirmadosSur != 0:
                print('No hubo regiones sin casos confirmados')

        elif opcion == 10:
            porcen_autoctonosSobreTotal = (contadorCasosAutoctonos * 100) / contadorCasosPositivos

            print('Porcentaje de casos positivos autoctonos sobre el total de casos: ', porcen_autoctonosSobreTotal, '%')

    print()
    print('=' * 80)
    print('PROGRAMA FINALIZADO')
    print('=' * 80)

#Script principal

test()