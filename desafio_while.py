contador = 0

empleados = 10

contador_masculinos_iot_ia = 0

contador_porcentaje = 0

nombre_masculino_mayor = ""
edad_masculino_mayor = 0
tecnologia_masculino_mayor = ""


while contador <= 9:

    nombre = input("Ingrese su nombre: ")

    edad = int(input("Ingrese la edad (mínimo 18): "))

    while edad < 18:
        edad = int(input("Edad invalida, tiene que ser mayor de 18 años, intente nuevamente: "))
    
    genero = input("Ingrese género (Masculino/Femenino/Otro): ")

    tecnologia = input("Ingrese la tecnologia que usted elija (IA, RV/RA, IOT): ")


    if genero == "Masculino" and edad >= 25 and edad <= 50 and (tecnologia == "IA" or tecnologia == "IOT"):

        contador_masculinos_iot_ia += 1
    
    if genero != "Femenino" and edad >= 33 and edad <= 40 and tecnologia != "IA":

        contador_porcentaje += 1

    if genero == "Masculino":
        
        if edad > edad_masculino_mayor:

            nombre_masculino_mayor = nombre
            edad_masculino_mayor = edad
            tecnologia_masculino_mayor = tecnologia

    contador += 1

porcentaje = (contador_porcentaje / empleados) * 100

print ("RESULTADOS DE LA ENCUESTA A 10 EMPLEADOS DE UTN TECHNOLOGIES")

print (f"{contador_masculinos_iot_ia} empleados masculinos entre 25 y 50 años votaron la tecnologia IOT o IA.")

print (f"El {porcentaje}% de empleados no femeninos entre 33 y 40 años no votaron por la tecnologia IA.")

print (F"{nombre_masculino_mayor} es el empleado mas grande que participo en la encuesta con {edad_masculino_mayor} y voto la tecnologia {tecnologia_masculino_mayor}.")






    

    


