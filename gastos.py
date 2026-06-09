saldo_disponible = input("Ingrese su saldo disponible: ")

saldo_disponible = float(saldo_disponible)

gasolina = 200
comida = 300
materiaprima = 105

total_gastos = gasolina + comida + materiaprima

saldo_final = saldo_disponible - total_gastos

if saldo_final >= saldo_disponible * 0.5:
    print("Tienes suficiente dinero para cubrir tus gastos")
    print("Saldo final:", saldo_final)
elif saldo_final == 0:
    print("No tienes dinero disponible después de cubrir tus gastos.")
else:
    print("No tienes suficiente dinero para cubrir tus gastos.")
    print("Saldo final:", saldo_final)
 