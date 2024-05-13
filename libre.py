import jmlab
print("que deceas convertir")
print("1. velocidad, 2. distancia, 3. tiempo 4.area, 5. volumen, 6. perimetro 7.gramos a moles 8. concentracionmolar 9. porcentajes, 10. balance")
distancia = 0 
tiempo = 0
velocidad = 0
opcion = input("que convercsuib quieres operar")


if opcion =="1":
    distancia = float(input("ingrese su distancia"))
    tiempo= float (input ("ingresar su tiempo"))
    print("tu velocidad  es: ",jmlab.velocidad(distancia,tiempo))

elif opcion =="2":
    velocidad = float(input("ingrese su velocidad"))
    tiempo= float (input ("ingresar su tiempo"))
    print("tu distancia  es: ",jmlab.distancia(velocidad,tiempo))

elif opcion =="3":
    distancia = float(input("ingrese su distancia"))
    velocidad= float (input ("ingresar su velocidad"))
    print("tu tiempo  es: ",jmlab.tiempo(distancia,velocidad))

elif opcion =="4":
    base = float(input("ingrese su base"))
    altura= float (input ("ingresar su altura"))
    print("tu area es: ",jmlab.area(altura,base))

elif opcion =="5":
    longitud = float(input("ingrese su longitud"))
    ancho= float (input ("ingresar su ancho"))
    altura= float (input ("ingresar su altura"))
    print("tu volumen es: ",jmlab.volumen(longitud,ancho,altura))

elif opcion =="6":
    lado1 = float(input("ingrese su lado1"))
    lado2= float (input ("ingresar su lado2"))    
    lado3 = float(input("ingrese su lado3"))
    lado4= float (input ("ingresar su lado4"))
    print("tu perimetro es: ",jmlab.perimetro(lado1,lado2,lado2,lado3))

elif opcion =="7":
    perimetro = float(input("ingrese su longitud"))
    ancho= float (input ("ingresar su ancho"))
    altura= float (input ("ingresar su altura"))
    print("su volumen es: ",jmlab.volumen(perimetro,ancho,altura))

elif opcion =="8":
    molesoluto = float(input("ingrese su molesoluto"))
    volumensolucion= float (input ("ingresar su volumensolucion"))
    print("tu concentracionmolar es",jmlab.concentración(molesoluto,volumensolucion))

elif opcion =="9":
    masa = float(input("ingrese su masa"))
    masamolar= float (input ("ingresar su masamolar"))
    print("su convercion de gramos a moles es: ",jmlab.gramosmoles(masa,masamolar))

elif opcion =="10":
    masa = float(input("ingrese su masa"))
    volumen= float (input ("ingresar su volumen"))
    print("su densidad es: ",jmlab.densidad(masa,volumen))