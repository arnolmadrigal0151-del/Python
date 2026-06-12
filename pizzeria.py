# --- SISTEMA DE PEDIDOS: ULISES PIZZAS (CON CANCELACIÓN OFICIAL) ---

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

ingredientes_disponibles = [
    "Jamón", "Atún", "Tocino", "Cebolla", "Elote", "Salchicha", 
    "Champiñón", "Salami", "Jitomate", "Chorizo", "Piña", 
    "Carne Molida", "Pimiento Morrón"
]

complementos_menu = {
    "1": {"nombre": "Refresco / Jugo del Valle", "precio": 30},
    "2": {"nombre": "Aderezo Chimichurri Chico", "precio": 25},
    "3": {"nombre": "Aderezo Chimichurri Botella", "precio": 60}
}

sabores_bebidas = {
    "1": "Coca-Cola Original", "2": "Coca-Cola Zero", "3": "Sidral Mundet",
    "4": "Sprite", "5": "Fanta", "6": "Jugo del Valle (Manzana)",
    "7": "Jugo del Valle (Durazno)", "8": "Jugo del Valle (Mango)"
}

print("=======================================")
print("=== BIENVENIDO A ULISES PIZZAS SISTEMA ===")
print("=======================================\n")

nombre_cliente = input("Nombre del cliente: ")
telefono = input("Teléfono: ")

total_a_pagar = 0
resumen_pedido = []
pedido_abortado_por_usuario = False  # Bandera para saber si se forzó la cancelación

print(f"\n¡Hola {nombre_cliente}! Vamos a tomar tu orden.")

ordenando_pizzas = True
grupo_pizza = 1

while ordenando_pizzas:
    print("\n---------------------------------------")
    print(f"🍕 CONFIGURANDO GRUPO DE PIZZAS #{grupo_pizza}")
    print("---------------------------------------")
    
    # === PASO 1: SELECCIÓN DEL TAMAÑO ===
    print("SELECCIONA EL TAMAÑO DE LA PIZZA:")
    for clave, datos in precios_tamanos.items():
        print(f"[{clave}] {datos['nombre']} ---- ${datos['precio']}")
    print("[0] No agregar más pizzas (Ir a bebidas)")
    print("[4] CANCELAR PEDIDO POR COMPLETO ❌")  # Nueva opción oficial de escape
    
    opcion_tamano = input("Elige una opción (0-4): ")

    if opcion_tamano == "4":
        print("\nAbortando el proceso de orden...")
        pedido_abortado_por_usuario = True
        break  # Rompe el ciclo por completo

    if opcion_tamano == "0":
        print("Se cerró la configuración de pizzas.")
        break 
        
    if opcion_tamano in precios_tamanos:
        tamano_elegido = precios_tamanos[opcion_tamano]["nombre"]
        precio_unitario_pizza = precios_tamanos[opcion_tamano]["precio"]
        
        if opcion_tamano == "1":
            print("\n📢 NOTA: Recuerda que la Micro Pizza solo incluye un máximo de 2 ingredientes.")
    else:
        print("Opción inválida. Intenta de nuevo.")
        continue

    # === PASO 2: SELECCIÓN DE LA ESPECIALIDAD ===
    reintentar_especialidad = True
    regresar_a_tamano = False
    
    while reintentar_especialidad:
        print("\nSELECCIONA LA ESPECIALIDAD DE TU PIZZA:")
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

    # === PASO 3: SECCIÓN DE INGREDIENTES ===
    ingredientes_elegidos = []
    es_personalizada = (opcion_tamano == "1" and opcion_esp == "5") or (opcion_tamano != "1" and opcion_esp == "13")
    quiere_ingredientes = False

    if opcion_tamano == "1":
        if opcion_esp == "5":
            print("\n--- ¡VAMOS A ARMAR TU MICRO PIZZA! ---")
            quiere_ingredientes = True
        else:
            print(f"\nHas seleccionado: {especialidad_elegida}.")
            print("Las especialidades en Micro Pizza ya incluyen sus 2 ingredientes correspondientes.")
    else:
        if es_personalizada:
            print("\n--- ¡VAMOS A ARMAR TU PIZZA! ---")
            quiere_ingredientes = True
        else:
            print(f"\nHas seleccionado: {especialidad_elegida}")
            respuesta = input(f"¿Deseas agregar algún ingrediente EXTRA a tu pizza? (si/no): ").strip().lower()
            if respuesta == "si":
                quiere_ingredientes = True

    if quiere_ingredientes:
        agregando = True
        while agregando:
            print("\nINGREDIENTES DISPONIBLES:")
            for i, ing in enumerate(ingredientes_disponibles, start=1):
                print(f"[{i}] {ing}")
            print("[0] Terminar de agregar ingredientes")
            
            seleccion = input("Selecciona el número del ingrediente: ")
            
            if seleccion == "0":
                if opcion_tamano == "1" and len(ingredientes_elegidos) == 0:
                    print("Debes elegir al menos 1 ingrediente para tu pizza armada.")
                    continue
                agregando = False
                
            elif seleccion.isdigit() and 1 <= int(seleccion) <= len(ingredientes_disponibles):
                ing_nombre = ingredientes_disponibles[int(seleccion) - 1]
                if ing_nombre not in ingredientes_elegidos:
                    ingredientes_elegidos.append(ing_nombre)
                    print(f"¡{ing_nombre} agregado!")
                else:
                    print(f"¡Ya habías agregado {ing_nombre}!")
                    
                if opcion_tamano == "1" and len(ingredientes_elegidos) == 2:
                    print(f"\n⚠️ Has alcanzado el límite de 2 ingredientes para tu Micro Pizza.")
                    print(f"Ingredientes seleccionados: {', '.join(ingredientes_elegidos)}")
                    
                    confirmacion = input("¿Tus ingredientes son correctos? (si / cambiar): ").strip().lower()
                    if confirmacion == "cambiar":
                        ingredientes_elegidos.clear()
                        print("\nSe han borrado los ingredientes. Selecciona de nuevo desde cero.")
                    else:
                        print("¡Ingredientes confirmados!")
                        agregando = False
            else:
                print("Opción no válida.")

    # === PASO 4: CONFIRMACIÓN DE CANTIDAD ===
    print("\n---------------------------------------")
    cant_input = input(f"¿Cuántas pizzas de este tipo ({tamano_elegido} de {especialidad_elegida}) deseas llevar?: ")
    if cant_input.isdigit() and int(cant_input) > 0:
        cantidad_pizzas = int(cant_input)
    else:
        print("Cantidad inválida. Se registrará como 1 pizza.")
        cantidad_pizzas = 1

    precio_total_grupo = precio_unitario_pizza * cantidad_pizzas
    total_a_pagar += precio_total_grupo

    texto_pizza = f"{cantidad_pizzas}x {tamano_elegido} de {especialidad_elegida}"
    if ingredientes_elegidos:
        texto_pizza += f" (Con: {', '.join(ingredientes_elegidos)})"
    resumen_pedido.append(f"{texto_pizza} (${precio_total_grupo})")

    # === PASO 5: ¿OTRA PIZZA O CANCELAR TODO? ===
    print("\n---------------------------------------")
    print("Opciones: [si] agregar otra pizza | [no] ir a bebidas | [cancelar] borrar todo")
    otra_pizza = input("¿Qué deseas hacer?: ").strip().lower()
    
    if otra_pizza == "cancelar":
        print("\nCancelando el pedido actual por completo...")
        pedido_abortado_por_usuario = True
        break
    elif otra_pizza != "si":
        ordenando_pizzas = False
    else:
        grupo_pizza += 1

# ========================================================
# Sección de Complementos (Solo si no se abortó el pedido)
# ========================================================
if not pedido_abortado_por_usuario:
    print("\n---------------------------------------")
    quiere_complementos = input("¿Deseas agregar bebidas o aderezos? (si/no): ").strip().lower()

    if quiere_complementos == "si":
        continuar_adicionales = True
        while continuar_adicionales:
            print("\nCOMPLEMENTOS DISPONIBLES:")
            for clave, datos in complementos_menu.items():
                print(f"[{clave}] {datos['nombre']} ---- ${datos['precio']}")
            print("[4] Terminar de agregar complementos")
            
            opcion_comp = input("Elige una opción (1-4): ")
            
            if opcion_comp == "1":
                print("\nSABORES DISPONIBLES:")
                for c_sabor, n_sabor in sabores_bebidas.items():
                    print(f"  [{c_sabor}] {n_sabor}")
                opcion_sabor = input("Selecciona el sabor de tu bebida (1-8): ")
                
                if opcion_sabor in sabores_bebidas:
                    sabor_elegido = sabores_bebidas[opcion_sabor]
                    
                    cant_bebida_input = input(f"¿Cuántos ({sabor_elegido}) deseas agregar?: ")
                    if cant_bebida_input.isdigit() and int(cant_bebida_input) > 0:
                        cant_bebida = int(cant_bebida_input)
                    else:
                        cant_bebida = 1
                    
                    comp_precio_total = complementos_menu["1"]["precio"] * cant_bebida
                    total_a_pagar += comp_precio_total
                    resumen_pedido.append(f"{cant_bebida}x {sabor_elegido} (${comp_precio_total})")
                    print(f"¡Agregado!: {cant_bebida}x {sabor_elegido}")
                else:
                    print("Sabor no válido. No se agregó la bebida.")
                    
            elif opcion_comp in ["2", "3"]:
                comp_nombre = complementos_menu[opcion_comp]["nombre"]
                
                cant_aderezo_input = input(f"¿Cuántos ({comp_nombre}) deseas agregar?: ")
                if cant_aderezo_input.isdigit() and int(cant_aderezo_input) > 0:
                    cant_aderezo = int(cant_aderezo_input)
                else:
                    cant_aderezo = 1
                    
                comp_precio_total = complementos_menu[opcion_comp]["precio"] * cant_aderezo
                total_a_pagar += comp_precio_total
                resumen_pedido.append(f"{cant_aderezo}x {comp_nombre} (${comp_precio_total})")
                print(f"¡Agregado!: {cant_aderezo}x {comp_nombre}")
                
            elif opcion_comp == "4":
                continuar_adicionales = False
            else:
                print("Opción no válida.")

# ========================================================
# IMPRESIÓN DEL TICKET FINAL / PANTALLA DE CANCELACIÓN
# ========================================================
if pedido_abortado_por_usuario or total_a_pagar == 0:
    print("\n=======================================")
    print("       ❌ ATENCIÓN: PEDIDO CANCELADO     ")
    print("=======================================")
    print(f"Cliente: {nombre_cliente}")
    print(f"Teléfono: {telefono}")
    print("---------------------------------------")
    print(" El proceso fue interrumpido por el usuario")
    print(" o el carrito quedó vacío ($0).")
    print(" Esta sesión ha sido completamente cerrada.")
    print(" NO se envió ninguna orden a cocina. ")
    print("=======================================")
else:
    print("\n=======================================")
    print("         TICKET DE PEDIDO ONLINE       ")
    print("=======================================")
    print(f"Cliente:   {nombre_cliente}")
    print(f"Teléfono:  {telefono}")
    print("Entrega:   Para recoger en Sucursal 🏪")
    print("---------------------------------------")
    print("Detalle del pedido:")
    for item in resumen_pedido:
        print(f" - {item}")
    print("---------------------------------------")
    print(f"TOTAL A COBRAR: ${total_a_pagar}")
    print("=======================================")
    print("   ¡Pedido listo para mandar a cocina! ")
    print("=======================================")
    