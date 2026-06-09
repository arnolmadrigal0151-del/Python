print("hola mundo")
nombre = "Arnol"
edad = 27
mexicano = True

print ("hola " + nombre)
print ("tengo " + str(edad) + " años")
print ("¿Soy mexicano? " + str(mexicano))

saldo = 500
if saldo > 100:
    print("compra aprobada")
else:
    print("fondos insuficientes")


 
saldo_raw = input("Ingrese su saldo: ")
if float(saldo_raw) > 100:
    print("compra aprobada")
    nuevo_saldo = float(saldo_raw) - 100
    print("Su nuevo saldo es: " + str(nuevo_saldo))
else:
    print("fondos insuficientes")