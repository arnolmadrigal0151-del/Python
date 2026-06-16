# --- SISTEMA DE PEDIDOS: ULISES PIZZAS (CON NOTAS ESPECIALES) ---
import datetime
import os  

precios_tamanos = {
    "1": {"nombre": "Micro Pizza (Máx 2 ing)", "precio": 45},
    "2": {"nombre": "Pizza Individual", "precio": 139},
    "3": {"nombre": "Pizza 30 CM", "precio": 239}
}

especialidades_completas = {
    "1": "Hawaiana", "2": "Veneciana", "3": "Clásica", 
    "4": "Alemana", "5": "Carnes Frías", "6": "Italiana", 
    "7": "Portuguesa", "8": "Ranchera", "9": "Mexicana", 
    "10": "Atún a la Mexicana", "11": "Vegetariana", "12": "Especial",
    "13": "¡Arma tu Pizza! (Personalizada)"
}

especialidades_micro = {
    "1": "Hawaiana", 
    "2": "Veneciana", 
    "3": "Clásica", 
    "4": "Alemana",
    "5": "¡Arma tu Pizza! (Personalizada)"
}

recetas_base = {
    "Hawaiana": ["Jamón", "Piña"],
    "Veneciana": ["Jamón", "Salchicha"],
    "Clásica": ["Salami", "Champiñón"],
    "Alemana": ["Salami", "Salchicha"],
    "Carnes Frías": ["Salami", "Salchicha", "Jamón"],
    "Italiana": ["Champiñón", "Jamón", "Piña"],
    "Portuguesa": ["Carne Molida", "Pimiento Morrón", "Jitomate", "Cebolla"],
    "Ranchera": ["Chorizo", "Pimiento Morrón", "Jitomate", "Cebolla"],
    "Mexicana": ["Jamón", "Pimiento Morrón", "Jitomate", "Cebolla"],
    "Atún a la Mexicana": ["Atún", "Pimiento Morrón", "Jitomate", "Cebolla"],
    "Vegetariana": ["Champiñón", "Pimiento Morrón", "Jitomate", "Cebolla"],
    "Especial": ["Salami", "Salchicha", "Champiñón", "Chorizo", "Carne Molida", "Jamón", "Piña"]
}

ingredientes_disponibles = [
    "Jamón", "Atún", "Tocino", "Cebolla", "Elote", "Salchicha", 
    "Champiñón", "Salami", "Jitomate", "Chorizo", "Piña", 
    "Carne Molida", "Pimiento Morrón", "Pepperoni"
]

complementos_menu = {
    "1": {"nombre": "Refresco / Jugo del Valle", "precio": 30},
    "2": {"nombre": "Dips (Aderezos) Chico", "precio": 25}, 
    "3": {"nombre": "Aderezo Chimichurri Botella", "precio": 60}
}

sabores_bebidas = {
    "1": "Coca-Cola Original", "2": "Coca-Cola Zero", "3": "Sidral Mundet",
    "4": "Sprite", "5": "Fanta", "6": "Jugo del Valle (Manzana)",
    "7": "Jugo del Valle (Durazno)", "8": "Jugo del Valle (Mango)"
}

sabores_dips = {
    "1": "Dip Chimichurri Chico",
    "2": "Dip Mango Habanero",
    "3": "Dip Buffalo Wings",
    "4": "Dip Ajo Parmesano",
    "5": "Dip BBQ"
}

print("=======================================")
print("=== BIENVENIDO A ULISES PIZZAS SISTEMA ===")
print("=======================================\n")

nombre_cliente = input("Nombre del cliente: ")
telefono = input("Teléfono: ")

resumen_pedido = []  
total_a_pagar = 0
pedido_abortado_por_usuario = False  
grupo_pizza = 1
notas_generales_pedido = "Ninguna"  # Variable para guardar las instrucciones

sistema_activo = True

while sistema_activo:
    
    # --- BLOQUE 1: SECCIÓN DE PIZZAS ---
    ordenando_pizzas = True
    while ordenando_pizzas:
        print("\n=======================================")
        print(f"🍕 CONFIGURANDO PIZZA(S) EN GRUPO #{grupo_pizza}")
        print("=======================================")
        
        print("\n📍 PROGRESO: [1. TAMAÑO] -> 2. Especialidad -> 3. Ingredientes -> 4. Cantidad")
        print("-------------------------------------------------------------------------")
        print("SELECCIONA EL TAMAÑO DE LA PIZZA:")
        for clave, datos in precios_tamanos.items():
            print(f"[{clave}] {datos['nombre']} ---- ${datos['precio']}")
        print("[0] No agregar más pizzas (Avanzar a Bebidas y Aderezos)")
        print("[4] CANCELAR PEDIDO POR COMPLETO ❌")  
        
        opcion_tamano = input("Elige una opción (0-4): ")

        if opcion_tamano == "4":
            print("\nAbortando el proceso de orden...")
            pedido_abortado_por_usuario = True
            sistema_activo = False
            break  

        if opcion_tamano == "0":
            print("\nPerfecto, cerramos la sección de pizzas.")
            break 
            
        if opcion_tamano in precios_tamanos:
            tamano_elegido = precios_tamanos[opcion_tamano]["nombre"]
            precio_unitario_pizza = precios_tamanos[opcion_tamano]["precio"]
            
            if opcion_tamano == "1":
                print("\n📢 NOTA: Recuerda que la Micro Pizza solo incluye un máximo de 2 ingredientes.")
        else:
            print("Opción inválida. Intenta de nuevo.")
            continue

        # Paso 2: Especialidad
        reintentar_especialidad = True
        regresar_a_tamano = False
        
        while reintentar_especialidad:
            print("\n📍 PROGRESO: 1. Tamaño -> [2. ESPECIALIDAD] -> 3. Ingredientes -> 4. Cantidad")
            print("-------------------------------------------------------------------------")
            print("SELECCIONA LA ESPECIALIDAD DE TU PIZZA:")
            if opcion_tamano == "1":
                menu_activo = especialidades_micro
                limite_opciones = "1-5"
            else:
                menu_activo = especialidades_completas
                limite_opciones = "1-13"

            for clave, nombre in menu_activo.items():
                print(f"[{clave}] {nombre}")
            print("[0] <-- REGRESAR A ELEGIR TAMAÑO")

            opcion_esp = input(f"Elige una opción o 0 para regresar ({limite_opciones}): ")

            if opcion_esp == "0":
                print("🔄 Regresando a la selección de tamaño...")
                regresar_a_tamano = True
                break 

            if opcion_esp in menu_activo:
                especialidad_elegida = menu_activo[opcion_esp]
                reintentar_especialidad = False 
            else:
                print("Opción inválida. Intenta de nuevo.")
                
        if regresar_a_tamano:
            continue 

        # Paso 3: Modificación de Ingredientes (Quitar Base, Agregar Extras y Queso Extra)
        ingredientes_actuales = []
        es_personalizada = (opcion_tamano == "1" and opcion_esp == "5") or (opcion_tamano != "1" and opcion_esp == "13")
        notas_modificacion = ""
        precio_adicional_queso = 0

        print("\n📍 PROGRESO: 1. Tamaño -> 2. Especialidad -> [3. INGREDIENTES] -> 4. Cantidad")
        print("-------------------------------------------------------------------------")

        if es_personalizada:
            print("--- ¡VAMOS A ARMAR TU PIZZA DESDE CERO! ---")
            agregando = True
            while agregando:
                print("\nINGREDIENTES DISPONIBLES:")
                for i, ing in enumerate(ingredientes_disponibles, start=1):
                    print(f"[{i}] {ing}")
                print("[0] Terminar de agregar ingredientes")
                
                seleccion = input("Selecciona el número del ingrediente: ")
                if seleccion == "0":
                    if len(ingredientes_actuales) == 0:
                        print("Debes elegir al menos 1 ingrediente para tu pizza personalizada.")
                        continue
                    agregando = False
                elif seleccion.isdigit() and 1 <= int(seleccion) <= len(ingredientes_disponibles):
                    ing_nombre = ingredientes_disponibles[int(seleccion) - 1]
                    if ing_nombre not in ingredientes_actuales:
                        ingredientes_actuales.append(ing_nombre)
                        print(f"¡{ing_nombre} agregado!")
                    else:
                        print(f"¡Ya habías agregado {ing_nombre}!")
                        
                    if opcion_tamano == "1" and len(ingredientes_actuales) == 2:
                        print(f"\n⚠️ Has alcanzado el límite de 2 ingredientes para tu Micro Pizza.")
                        agregando = False
                else:
                    print("Opción no válida.")
        else:
            if especialidad_elegida in recetas_base:
                ingredientes_actuales = list(recetas_base[especialidad_elegida])
            
            print(f"Has seleccionado: Pizza {especialidad_elegida}.")
            print(f"Ingredientes que incluye de base: {', '.join(ingredientes_actuales)}")
            
            # Sub-Paso A: Quitar ingredientes base
            quitar_respuesta = input("¿Deseas QUITAR algún ingrediente de base? (si/no): ").strip().lower()
            if quitar_respuesta == "si":
                quitando = True
                ingredientes_quitados = []
                while quitando and len(ingredientes_actuales) > 0:
                    print("\n¿Cuál ingrediente deseas retirar de la receta?")
                    for idx, ing in enumerate(ingredientes_actuales, start=1):
                        print(f" [{idx}] {ing}")
                    print(" [0] Dejar de quitar ingredientes")
                    
                    opcion_quitar = input("Elige el número a retirar: ").strip()
                    if opcion_quitar == "0":
                        quitando = False
                    elif opcion_quitar.isdigit() and 1 <= int(opcion_quitar) <= len(ingredientes_actuales):
                        removido = ingredientes_actuales.pop(int(opcion_quitar) - 1)
                        ingredientes_quitados.append(removido)
                        print(f"❌ Removido: Sin {removido}")
                    else:
                        print("Opción inválida.")
                
                if ingredientes_quitados:
                    notas_modificacion += f" (SIN: {', '.join(ingredientes_quitados)})"

            # Sub-Paso B: Ingredientes extras (Excluyendo Micro Pizza)
            if opcion_tamano != "1":
                agregar_respuesta = input("\n¿Deseas agregar algún ingrediente EXTRA a tu pizza? (si/no): ").strip().lower()
                if agregar_respuesta == "si":
                    agregando_extras = True
                    ingredientes_extras = []
                    while agregando_extras:
                        print("\nINGREDIENTES DISPONIBLES PARA EXTRA:")
                        for i, ing in enumerate(ingredientes_disponibles, start=1):
                            print(f"[{i}] {ing}")
                        print("[0] Terminar de añadir extras")
                        
                        seleccion = input("Selecciona el número del ingrediente extra: ")
                        if seleccion == "0":
                            agregando_extras = False
                        elif seleccion.isdigit() and 1 <= int(seleccion) <= len(ingredientes_disponibles):
                            ing_nombre = ingredientes_disponibles[int(seleccion) - 1]
                            if ing_nombre not in ingredientes_extras:
                                ingredientes_extras.append(ing_nombre)
                                ingredientes_actuales.append(ing_nombre)
                                print(f"¡{ing_nombre} anotado como extra!")
                            else:
                                print(f"¡Ya agregaste {ing_nombre} como extra!")
                        else:
                            print("Opción no válida.")
                    
                    if ingredientes_extras:
                        notas_modificacion += f" (CON EXTRA: {', '.join(ingredientes_extras)})"

        # Sub-Paso C: Lógica de Queso Extra
        if opcion_tamano != "1":
            costo_queso = 15 if opcion_tamano == "2" else 30
            print(f"\n🧀 OPCIÓN ADICIONAL: Queso Extra para tamaño {tamano_elegido} cuesta ${costo_queso}")
            quiere_queso = input(f"¿Deseas agregar Queso Extra por ${costo_queso}? (si/no): ").strip().lower()
            if quiere_queso == "si":
                precio_adicional_queso = costo_queso
                notas_modificacion += " (+ QUESO EXTRA 🧀)"
                print("¡Queso extra añadido a la receta!")

        # Paso 4: Cantidad
        print("\n📍 PROGRESO: 1. Tamaño -> 2. Especialidad -> 3. Ingredientes -> [4. CANTIDAD]")
        print("-------------------------------------------------------------------------")
        cant_input = input(f"¿Cuántas pizzas de este tipo ({tamano_elegido} de {especialidad_elegida}) deseas llevar?: ")
        if cant_input.isdigit() and int(cant_input) > 0:
            cantidad_pizzas = int(cant_input)
        else:
            print("Cantidad inválida. Se registrará como 1 pizza.")
            cantidad_pizzas = 1

        precio_final_unitario = precio_unitario_pizza + precio_adicional_queso
        precio_total_grupo = precio_final_unitario * cantidad_pizzas
        total_a_pagar += precio_total_grupo

        texto_pizza = f"{cantidad_pizzas}x {tamano_elegido} de {especialidad_elegida}"
        if es_personalizada:
            texto_pizza += f" (Con: {', '.join(ingredientes_actuales)})"
            if precio_adicional_queso > 0:
                texto_pizza += " (+ QUESO EXTRA 🧀)"
        elif notas_modificacion:
            texto_pizza += notas_modificacion
        
        resumen_pedido.append({"texto": texto_pizza, "precio": precio_total_grupo})

        print("\n🛒 CARRITO PARCIAL:")
        for idx, item in enumerate(resumen_pedido, start=1):
            print(f"  {idx}. {item['texto']} (${item['precio']})")
        print(f"  Subtotal actual: ${total_a_pagar}")

        print("\n-------------------------------------------------------------------------")
        print("Opciones: [si] agregar otra pizza | [no] ir a bebidas y aderezos | [cancelar] borrar todo")
        otra_pizza = input("¿Qué deseas hacer?: ").strip().lower()
        
        if otra_pizza == "cancelar":
            print("\nCancelando el pedido actual por completo...")
            pedido_abortado_por_usuario = True
            sistema_activo = False
            break
        elif otra_pizza != "si":
            ordenando_pizzas = False
        else:
            grupo_pizza += 1

    if pedido_abortado_por_usuario:
        break

    # --- BLOQUE 2: SECCIÓN DE COMPLEMENTOS ---
    print("\n=======================================")
    print("🥤 SECCIÓN DE BEBIDAS Y ADEREZOS")
    print("=======================================")
    quiere_complementos = input("¿Deseas agregar bebidas o aderezos a tu orden? (si/no): ").strip().lower()

    if quiere_complementos == "si":
        continuar_adicionales = True
        while continuar_adicionales:
            print("\nCOMPLEMENTOS DISPONIBLES:")
            for clave, datos in complementos_menu.items():
                print(f"[{clave}] {datos['nombre']} ---- ${datos['precio']}")
            print("[4] Terminar y proceder al resumen del pedido 🧾")
            
            opcion_comp = input("Elige una opción (1-4): ")
            
            if opcion_comp == "1":
                print("\nSABORES DISPONIBLES:")
                for c_sabor, n_sabor in sabores_bebidas.items():
                    print(f"  [{c_sabor}] {n_sabor}")
                opcion_sabor = input("Selecciona el sabor de tu bebida (1-8): ")
                
                if opcion_sabor in sabores_bebidas:
                    sabor_elegido = sabores_bebidas[opcion_sabor]
                    cant_bebida_input = input(f"¿Cuántos ({sabor_elegido}) deseas agregar?: ")
                    cant_bebida = int(cant_bebida_input) if cant_bebida_input.isdigit() and int(cant_bebida_input) > 0 else 1
                    comp_precio_total = complementos_menu["1"]["precio"] * cant_bebida
                    total_a_pagar += comp_precio_total
                    resumen_pedido.append({"texto": f"{cant_bebida}x {sabor_elegido}", "precio": comp_precio_total})
                    print(f"¡Agregado!: {cant_bebida}x {sabor_elegido}")
                else:
                    print("Sabor no válido.")
                    
            elif opcion_comp == "2":  
                print("\nSABORES DE ADEREZOS (DIPS) DISPONIBLES ($25 c/u):")
                for c_dip, n_dip in sabores_dips.items():
                    print(f"  [{c_dip}] {n_dip}")
                opcion_dip = input("Selecciona el sabor del aderezo (1-5): ")
                
                if opcion_dip in sabores_dips:
                    dip_elegido = sabores_dips[opcion_dip]
                    cant_dip_input = input(f"¿Cuántos ({dip_elegido}) deseas agregar?: ")
                    cant_dip = int(cant_dip_input) if cant_dip_input.isdigit() and int(cant_dip_input) > 0 else 1
                    comp_precio_total = complementos_menu["2"]["precio"] * cant_dip
                    total_a_pagar += comp_precio_total
                    resumen_pedido.append({"texto": f"{cant_dip}x {dip_elegido}", "precio": comp_precio_total})
                    print(f"¡Agregado!: {cant_dip}x {dip_elegido}")
                else:
                    print("Opción no válida.")
                
            elif opcion_comp == "3":
                comp_nombre = complementos_menu[opcion_comp]["nombre"]
                cant_aderezo_input = input(f"¿Cuántos ({comp_nombre}) deseas agregar?: ")
                cant_aderezo = int(cant_aderezo_input) if cant_aderezo_input.isdigit() and int(cant_aderezo_input) > 0 else 1
                comp_precio_total = complementos_menu[opcion_comp]["precio"] * cant_aderezo
                total_a_pagar += comp_precio_total
                resumen_pedido.append({"texto": f"{cant_aderezo}x {comp_nombre}", "precio": comp_precio_total})
                print(f"¡Agregado!: {cant_aderezo}x {comp_nombre}")
                
            elif opcion_comp == "4":
                continuar_adicionales = False

    # 📝 🛠️ SECCIÓN NUEVA: INSTRUCCIONES O NOTAS DE ENTREGA (Antes del Cierre)
    if len(resumen_pedido) > 0:
        print("\n=======================================")
        print("✍️  INSTRUCCIONES ESPECIALES DE ENTREGA")
        print("=======================================")
        quiere_dejar_nota = input("¿Deseas agregar alguna indicación extra para tu pedido? (si/no): ").strip().lower()
        if quiere_dejar_nota == "si":
            notas_generales_pedido = input("Escribe tu nota aquí (ej. 'Pasaré a las 4pm', 'Pizza bien dorada'): ").strip()
            if not notas_generales_pedido:
                notas_generales_pedido = "Ninguna"
            else:
                print("¡Nota guardada con éxito!")

    # --- BLOQUE 3: MENÚ DE CIERRE ---
    if len(resumen_pedido) > 0:
        print("\n=======================================")
        print("       📋 RESUMEN DE TU ORDEN          ")
        print("=======================================")
        print(f"Cliente:   {nombre_cliente}")
        print(f"Teléfono:  {telefono}")
        print(f"Notas:     {notas_generales_pedido}") # <-- Ahora el usuario la ve antes de pagar
        print("---------------------------------------")
        for idx, item in enumerate(resumen_pedido, start=1):
            print(f" [{idx}] {item['texto']} ---- ${item['precio']}")
        print("---------------------------------------")
        print(f"TOTAL HASTA EL MOMENTO: ${total_a_pagar}")
        print("=======================================")
        
        print("¿Qué deseas hacer con esta orden?")
        print("[1] SÍ, confirmar y mandar a cocina 🚀")
        print("[2] MODIFICAR / AGREGAR O QUITAR PRODUCTOS 🔄")
        print("[3] CANCELAR pedido por completo y vaciar carrito ❌")
        
        decision = input("Elige una opción (1-3): ").strip()

        if decision == "1":
            sistema_activo = False 
        elif decision == "2":
            print("\n---------------------------------------")
            print("⚙️ MENÚ DE MODIFICACIÓN DE CARRITO")
            print("---------------------------------------")
            print("[1] Agregar más cosas al pedido")
            print("[2] Eliminar un producto erróneo del carrito 🗑️")
            sub_decision = input("Elige una opción (1-2): ").strip()

            if sub_decision == "2":
                print("\n--- ELIMINAR ELEMENTO ---")
                for idx, item in enumerate(resumen_pedido, start=1):
                    print(f" [{idx}] {item['texto']} (${item['precio']})")
                borrar_idx = input("\nDigita el número del producto que deseas ELIMINAR: ")
                
                if borrar_idx.isdigit() and 1 <= int(borrar_idx) <= len(resumen_pedido):
                    eliminado = resumen_pedido.pop(int(borrar_idx) - 1)
                    total_a_pagar -= eliminado['precio']
                    print(f"\n🗑️ Se eliminó con éxito: {eliminado['texto']}")
                else:
                    print("\nNúmero inválido.")
            
            grupo_pizza += 1
            continue
        else:
            pedido_abortado_por_usuario = True
            sistema_activo = False
    else:
        total_a_pagar = 0
        sistema_activo = False

# ========================================================
# PROCESAMIENTO FINAL (FUERA DEL BUCLE)
# ========================================================
if pedido_abortado_por_usuario or total_a_pagar == 0:
    print("\n=======================================")
    print("       ❌ ATENCIÓN: PEDIDO CANCELADO     ")
    print("=======================================")
    print(" El proceso fue interrumpido de forma segura. NO se mandó nada.")
    print("=======================================")
else:
    ahora = datetime.datetime.now()
    fecha_texto = ahora.strftime("%Y-%m-%d %H:%M:%S")
    fecha_archivo = ahora.strftime("%Y%m%d_%H%M%S") 

    texto_ticket = f"""=======================================
         TICKET DE PEDIDO ONLINE       
=======================================
Fecha/Hora: {fecha_texto}
Cliente:   {nombre_cliente}
Teléfono:  {telefono}
Entrega:   Para recoger en Sucursal 🏪
Notas Obs: {notas_generales_pedido}
---------------------------------------
Detalle del pedido:
"""
    for item in resumen_pedido:
        texto_ticket += f" - {item['texto']} (${item['precio']})\n"
        
    texto_ticket += f"""---------------------------------------
TOTAL A COBRAR: ${total_a_pagar}
=======================================
   ¡Pedido listo para mandar a cocina! 
======================================="""

    print("\n" + texto_ticket)

    nombre_carpeta = "pedidos"
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)

    nombre_archivo = f"pedido_{nombre_cliente.replace(' ', '_')}_{fecha_archivo}.txt"
    ruta_completa = os.path.join(nombre_carpeta, nombre_archivo)
    
    try:
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            archivo.write(texto_ticket)
        print(f"\n💾 [SISTEMA] Ticket respaldado en: {ruta_completa}")
    except Exception as e:
        print(f"\n⚠️ [ERROR] No se pudo guardar el archivo: {e}")
        