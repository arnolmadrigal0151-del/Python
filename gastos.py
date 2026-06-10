# 1. Definimos el presupuesto mensual base y el semanal de consulta
presupuesto_mensual = 9388.00
presupuesto_semanal = 2347.00

# El dinero disponible para el mes empezará con el total mensual
dinero_disponible_mes = presupuesto_mensual

# Nuestra lista para guardar los registros
mis_gastos = []


# 2. REGISTRO DE GASTOS (Calculados a nivel mensual)

# --- Gasto Semanal (Moto) ---
gasto_moto_mensual = 500.00 * 4
dinero_disponible_mes -= gasto_moto_mensual
mis_gastos.append({"descripcion": "Abono de la moto (Mensualizado)", "monto": gasto_moto_mensual})

# --- Gasto Semanal (Cachafla / Gusgueras) ---
gasto_cachafla_mensual = 300.00 * 4
dinero_disponible_mes -= gasto_cachafla_mensual
mis_gastos.append({"descripcion": "Cachafla / Gusgueras (Mensualizado)", "monto": gasto_cachafla_mensual})

# --- Gasto Quincenal (Gasolina) ---
gasto_gasolina_mensual = 200.00 * 2
dinero_disponible_mes -= gasto_gasolina_mensual
mis_gastos.append({"descripcion": "Gasolina (Mensualizado)", "monto": gasto_gasolina_mensual})

# --- Gasto Quincenal  (Nelo) ---
# Al ser pago único de junio, no lo multiplicamos por nada
gasto_nelo = 855.00
dinero_disponible_mes -= gasto_nelo
mis_gastos.append({"descripcion": "Nelo (Pago único)", "monto": gasto_nelo})

# --- Gasto Quincenal (Gasto acá) ---
gasto_aca_mensual = 150.00 * 2
dinero_disponible_mes -= gasto_aca_mensual
mis_gastos.append({"descripcion": "Gasto acá (Mensualizado)", "monto": gasto_aca_mensual})

# --- Gasto Mensual (Internet) ---
gasto_internet = 689.00
dinero_disponible_mes -= gasto_internet
mis_gastos.append({"descripcion": "Pago de Internet", "monto": gasto_internet})

# --- Gasto Mensual (Mercado Libre) ---
gasto_mercadolibre = 1112.00
dinero_disponible_mes -= gasto_mercadolibre
mis_gastos.append({"descripcion": "Abono Mercado Libre", "monto": gasto_mercadolibre})


# 3. MOSTRAR RESULTADOS en la pantalla
# Calculamos cuánto dinero libre te queda por semana realmente
dinero_libre_semanal = dinero_disponible_mes / 4

print(f"--- RESUMEN DE PRESUPUESTO ---")
print(f"Presupuesto Semanal de referencia: ${presupuesto_semanal} pesos.")
print(f"Presupuesto Mensual Inicial: ${presupuesto_mensual} pesos.")
print(f"--------------------------------")
print(f"Dinero disponible en el mes: ${dinero_disponible_mes} pesos.")
print(f"💵 Tu presupuesto libre real para gastar es de: ${dinero_libre_semanal} pesos por semana.")
print(f"--------------------------------")
print("📋 DESGLOSE DE GASTOS REGISTRADOS:")

# Este bucle 'for' recorre tu lista y muestra cada gasto ordenado
for gasto in mis_gastos:
    print(f"• {gasto['descripcion']}: ${gasto['monto']} pesos.")
    