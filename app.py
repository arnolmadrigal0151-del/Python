try:
    import streamlit as st
    import urllib.parse  # 👈 Ponla justo aquí
except Exception:
    # Fallback stub for environments where streamlit is not installed
    class _DummySessionState(dict):
        pass

    class _DummySt:
        session_state = _DummySessionState()

        def set_page_config(self, *args, **kwargs):
            return None

    st = _DummySt()

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Ulises Pizzas", page_icon="🍕", layout="centered")

# Inicializar estados de sesión esenciales
if "carrito" not in st.session_state:
    st.session_state.carrito = []

if "form_pizza_id" not in st.session_state:
    st.session_state.form_pizza_id = 0

# --- 2. DATOS DEL MENÚ OFICIAL (Precios en MXN) ---
precios_tamanos = {
    "Pizza Grande (30 cm)": 239,
    "Pizza Individual": 139,
    "Micro Pizza (Máx 2 ing)": 45
}

recetas_ingredientes = {
    "Hawaiana": ["Jamón", "Piña"],
    "Veneciana": ["Salchicha", "Jamón"],
    "Clásica": ["Salami", "Champiñón"],
    "Alemana": ["Salami", "Salchicha"],
    "Carnes Frías": ["Salami", "Salchicha", "Jamón"],
    "Italiana": ["Champiñón", "Jamón", "Piña"],
    "Portuguesa": ["Carne Molida", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Ranchera": ["Chorizo", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Mexicana": ["Jamón", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Atún a la Mexicana": ["Atún", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Vegetariana": ["Champiñón", "Jitomate", "Cebolla", "Pimiento Morrón"],
    "Especial": ["Salami", "Salchicha", "Champiñón", "Carne Molida", "Chorizo", "Jamón", "Piña"],
    "¡Arma tu Pizza! (Personalizada)": []
}

ingredientes_disponibles = [
    "Jamón", "Atún", "Tocino", "Cebolla", "Elote", "Salchicha", 
    "Champiñón", "Salami", "Jitomate", "Chorizo", "Piña", 
    "Carne Molida", "Pimiento Morrón", "Pepperoni"
]

bebidas_precios = {
    "Coca Cola original": 30, "Coca Cola Zero": 30, "Sprite": 30, "Sidral Mundet": 30,
    "Fanta": 30, "Jugo del Valle Mango": 30, "Jugo del Valle Manzana": 30, "Jugo del Valle Durazno": 30
}

aderezos_precios = {
    "Aderezo chimichurri botella grande": 60, "Aderezo chimichurri": 25, "Aderezo mango habanero": 25,
    "Aderezo ajo parmesano": 25, "Aderezo BBQ": 25, "Aderezo buffalo": 25
}

# --- 3. DISEÑO DE LA INTERFAZ VISUAL ---
st.title("🍕 Ulises Pizzas - Sistema de Pedidos")
st.markdown("---")

st.subheader("👤 Datos de la Orden")
col1, col2 = st.columns(2)
with col1:
    nombre_cliente = st.text_input("Nombre del Cliente:", placeholder="Ej. Arnol Madrigal")
with col2:
    telefono = st.text_input("Teléfono de Contacto:", placeholder="Ej. 3329893703")

st.markdown("---")

# =========================================================
# SECCIÓN A: CONFIGURADOR DE PIZZAS (EL MOSTRADOR)
# =========================================================
st.subheader("🍕 Configura una Pizza")

fid = st.session_state.form_pizza_id

tamano_seleccionado = st.selectbox("Selecciona el Tamaño:", list(precios_tamanos.keys()), key=f"tam_{fid}")
precio_pizza_base = precios_tamanos[tamano_seleccionado]
es_micro = (tamano_seleccionado == "Micro Pizza (Máx 2 ing)")

if es_micro:
    especialidades_disponibles = ["Hawaiana", "Veneciana", "Clásica", "Alemana", "¡Arma tu Pizza! (Personalizada)"]
else:
    especialidades_disponibles = list(recetas_ingredientes.keys())

hacer_mitad = False
if not es_micro:
    hacer_mitad = st.checkbox("🌓 ¿Quieres tu pizza mitad y mitad?", key=f"mitad_{fid}")

especialidad_final_nombre = ""
detalles_ingredientes_visibles = ""
ingredientes_finales_a = []
ingredientes_finales_b = []

if hacer_mitad:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("### 🌓 Mitad A")
        especialidad_a = st.selectbox("Especialidad Mitad A:", options=especialidades_disponibles, key=f"sel_mitad_a_{fid}")
        if especialidad_a == "¡Arma tu Pizza! (Personalizada)":
            st.caption("Selecciona los ingredientes para la Mitad A:")
            for ing in ingredientes_disponibles:
                if st.checkbox(ing, key=f"ing_a_{ing}_{fid}"):
                    ingredientes_finales_a.append(ing)
        else:
            ingredientes_finales_a = recetas_ingredientes[especialidad_a]
            st.info(f" Lleva: {', '.join(ingredientes_finales_a)}")
            
    with col_m2:
        st.markdown("### 🌗 Mitad B")
        especialidad_b = st.selectbox("Especialidad Mitad B:", options=especialidades_disponibles, key=f"sel_mitad_b_{fid}")
        if especialidad_b == "¡Arma tu Pizza! (Personalizada)":
            st.caption("Selecciona los ingredientes para la Mitad B:")
            for ing in ingredientes_disponibles:
                if st.checkbox(ing, key=f"ing_b_{ing}_{fid}"):
                    ingredientes_finales_b.append(ing)
        else:
            ingredientes_finales_b = recetas_ingredientes[especialidad_b]
            st.info(f" Lleva: {', '.join(ingredientes_finales_b)}")

    especialidad_final_nombre = f"{especialidad_a} (Mitad: {especialidad_b})"
    detalles_ingredientes_visibles = f"**Mitad A ({especialidad_a}):** {', '.join(ingredientes_finales_a) if ingredientes_finales_a else 'Solo Queso'} | **Mitad B ({especialidad_b}):** {', '.join(ingredientes_finales_b) if ingredientes_finales_b else 'Solo Queso'}"

else:
    especialidad_seleccionada = st.selectbox("Selecciona la Especialidad:", options=especialidades_disponibles, key=f"esp_{fid}")
    especialidad_final_nombre = especialidad_seleccionada
    ingredientes_base = recetas_ingredientes[especialidad_seleccionada]
    
    ingredientes_quitar = []
    ingredientes_agregar = []
    ingredientes_finales_a = list(ingredientes_base)

    if especialidad_seleccionada != "¡Arma tu Pizza! (Personalizada)":
        st.info(f"**Receta base actual:** 🧀 Queso, {', '.join(ingredientes_base)}")
        if not es_micro:
            col_q, col_a = st.columns(2)
            with col_q:
                ingredientes_quitar = st.multiselect("❌ ¿Quitar ingredientes de la receta base?", ingredientes_base, key=f"quit_{fid}")
            with col_a:
                opciones_agregar = [i for i in ingredientes_disponibles if i not in ingredientes_base]
                ingredientes_agregar = st.multiselect("➕ ¿Agregar ingredientes extra?", opciones_agregar, key=f"add_{fid}")
            
            for ing in ingredientes_quitar:
                if ing in ingredientes_finales_a: ingredientes_finales_a.remove(ing)
            for ing in ingredientes_agregar:
                ingredientes_finales_a.append(ing)
        detalles_ingredientes_visibles = f"Ingredientes: {', '.join(ingredientes_finales_a)}"
    else:
        st.info("**Receta base actual:** ¡Tú eliges la combinación perfecta! Base de salsa y queso incluida.")
        if es_micro:
            st.warning("⚠️ Recuerda: La Micro Pizza solo permite un máximo de 2 ingredientes.")
        
        cols = st.columns(3)
        ingredientes_finales_a = []
        for idx, ing in enumerate(ingredientes_disponibles):
            with cols[idx % 3]:
                if st.checkbox(ing, key=f"build_{ing}_{fid}"):
                    ingredientes_finales_a.append(ing)
        detalles_ingredientes_visibles = f"Ingredientes personalizados: {', '.join(ingredientes_finales_a) if ingredientes_finales_a else 'Solo Queso'}"

queso_extra = False
precio_queso_extra = 0
if not es_micro:
    costo_q = 30 if tamano_seleccionado == "Pizza Grande (30 cm)" else 15
    queso_extra = st.checkbox(f"🧀 ¡Agregar Queso Extra a toda la pizza! (+${costo_q} MXN)", key=f"q_extra_{fid}")
    precio_queso_extra = costo_q if queso_extra else 0

precio_esta_pizza = precio_pizza_base + precio_queso_extra

st.markdown("---")

# Creamos un contenedor limpio y aislado para la vista previa
with st.container():
    st.markdown("### 👀 Vista previa de tu pizza:")
    st.markdown(f"""
    > **Tamaño:** {tamano_seleccionado}  
    > **Estructura:** {'🌓 Mitad y Mitad' if hacer_mitad else '🍕 Pizza Completa'}  
    > **Detalle:** {especialidad_final_nombre} {'*(Con Queso Extra 🧀)*' if queso_extra else ''}  
    > **Configuración Real:** {detalles_ingredientes_visibles}  
    > **Precio de esta Pizza:** **${precio_esta_pizza} MXN**
    """)

if st.button("➕ AGREGAR PIZZA AL PEDIDO", use_container_width=True, type="secondary"):
    if es_micro and len(ingredientes_finales_a) > 2:
        st.error("⚠️ No se puede agregar. La Micro Pizza excede los 2 ingredientes.")
    elif not hacer_mitad and especialidad_final_nombre == "¡Arma tu Pizza! (Personalizada)" and len(ingredientes_finales_a) == 0:
        st.error("⚠️ Elige al menos 1 ingrediente para armar tu pizza.")
    elif hacer_mitad and (especialidad_a == "¡Arma tu Pizza! (Personalizada)" and len(ingredientes_finales_a) == 0):
        st.error("⚠️ Agrega al menos 1 ingrediente en la Mitad A.")
    elif hacer_mitad and (especialidad_b == "¡Arma tu Pizza! (Personalizada)" and len(ingredientes_finales_b) == 0):
        st.error("⚠️ Agrega al menos 1 ingrediente en la Mitad B.")
    else:
        nueva_pizza = {
            "tamano": tamano_seleccionado,
            "especialidad": especialidad_final_nombre,
            "queso_extra": queso_extra,
            "resumen_visual": detalles_ingredientes_visibles,
            "precio": precio_esta_pizza
        }
        st.session_state.carrito.append(nueva_pizza)
        st.session_state.form_pizza_id += 1
        st.rerun()

st.markdown("---")

# =========================================================
# SECCIÓN B: COMPLEMENTOS (Movida arriba del carrito para capturar datos)
# =========================================================
st.subheader("🥤 Bebidas y Aderezos Extra")
col_b, col_ad = st.columns(2)

bebidas_pedido = {}
total_bebidas_costo = 0
cantidad_total_bebidas = 0

with col_b:
    with st.expander("🥤 Desplegar Menú de Bebidas", expanded=False):
        for bebida, precio in bebidas_precios.items():
            cant = st.number_input(f"{bebida} (${precio} c/u)", min_value=0, max_value=10, value=0, key=f"beb_{bebida}")
            if cant > 0:
                bebidas_pedido[bebida] = cant
                total_bebidas_costo += precio * cant
                cantidad_total_bebidas += cant

aderezos_pedido = {}
total_aderezos_costo = 0
cantidad_total_aderezos = 0

with col_ad:
    with st.expander("🍯 Desplegar Menú de Aderezos", expanded=False):
        for aderezo, precio in aderezos_precios.items():
            cant = st.number_input(f"{aderezo} (${precio} c/u)", min_value=0, max_value=10, value=0, key=f"ade_{aderezo}")
            if cant > 0:
                aderezos_pedido[aderezo] = cant
                total_aderezos_costo += precio * cant
                cantidad_total_aderezos += cant

st.markdown("---")

# =========================================================
# SECCIÓN C: EL CARRITO DE COMPRAS INTEGRAL EN TIEMPO REAL
# =========================================================
st.subheader("🛒 Tu Carrito de Compras Actual")
total_general = 0

# Contenedor gris tipo recibo para agrupar todo lo seleccionado
with st.container(border=True):
    hay_articulos = False
    
    # 1. Mostrar Pizzas en el Carrito
    if st.session_state.carrito:
        hay_articulos = True
        st.markdown("**🍕 Pizzas Seleccionadas:**")
        for index, pizza in enumerate(st.session_state.carrito):
            col_item, col_btn = st.columns([6, 1])
            with col_item:
                detalles = f"**{pizza['tamano']}** de {pizza['especialidad']}"
                if pizza['queso_extra']:
                    detalles += " *(+Queso Extra 🧀)*"
                detalles += f"<br><small style='color:gray;'>└─ {pizza['resumen_visual']}</small>"
                st.markdown(f"• {detalles} — **${pizza['precio']} MXN**", unsafe_allow_html=True)
                total_general += pizza['precio']
            with col_btn:
                if st.button("🗑️", key=f"del_{index}"):
                    st.session_state.carrito.pop(index)
                    st.rerun()
        st.markdown(" ")

    # 2. Mostrar Bebidas en Tiempo Real (Sin necesidad de botón de agregar)
    if bebidas_pedido:
        hay_articulos = True
        st.markdown("**🥤 Bebidas:**")
        for bebida, cant in bebidas_pedido.items():
            costo_b = bebidas_precios[bebida] * cant
            st.markdown(f"• {cant}x {bebida} — **${costo_b} MXN**")
            total_general += costo_b
        st.markdown(" ")

    # 3. Mostrar Aderezos en Tiempo Real
    if aderezos_pedido:
        hay_articulos = True
        st.markdown("**🍯 Aderezos:**")
        for aderezo, cant in aderezos_pedido.items():
            costo_a = aderezos_precios[aderezo] * cant
            st.markdown(f"• {cant}x {aderezo} — **${costo_a} MXN**")
            total_general += costo_a

    if not hay_articulos:
        st.info("El carrito está completamente vacío. Configura tu orden arriba.")
    else:
        st.markdown("---")
        st.markdown(f"### Total de la Orden: :green[${total_general} MXN]")

st.markdown("---")
st.subheader("✍️ Instrucciones Especiales")
notas_pedido = st.text_area("¿Alguna indicación para cocina?", placeholder="Ej. El aderezo BBQ que vaya aparte por favor...")
st.markdown("---")

# --- 4. ENVÍO DE TICKET FINAL ---
if st.button("🚀 ENVIAR MI PEDIDO COMPLETO", use_container_width=True, type="primary"):
    if not nombre_cliente or not telefono:
        st.error("⚠️ Por favor, escribe tu nombre y teléfono antes de mandar el pedido.")
    elif not st.session_state.carrito and not bebidas_pedido and not aderezos_pedido:
        st.error("⚠️ Tu carrito está vacío. Agrega una pizza o un complemento antes de enviar.")
    else:
        # 1. Generar el desglose del texto para la pantalla y para WhatsApp
        resumen_pizzas_txt = ""
        for p in st.session_state.carrito:
            modificaciones = " (CON QUESO EXTRA 🧀)" if p['queso_extra'] else ""
            resumen_pizzas_txt += f"\n* 1x {p['tamano']} de {p['especialidad']}{modificaciones}\n  └─ {p['resumen_visual']} -> ${p['precio']} MXN"

        lista_bebidas_txt = [f"{cant}x {bebida}" for bebida, cant in bebidas_pedido.items()]
        texto_bebidas = ", ".join(lista_bebidas_txt) if lista_bebidas_txt else "Ninguna"

        lista_aderezos_txt = [f"{cant}x {aderezo}" for aderezo, cant in aderezos_pedido.items()]
        texto_aderezos = ", ".join(lista_aderezos_txt) if lista_aderezos_txt else "Ninguno"

        # 2. Armar el mensaje de texto limpio y formateado con negritas para WhatsApp
        mensaje_whatsapp = f"""🍕 *NUEVO PEDIDO - ULISES PIZZAS* 🍕
--------------------------------
👤 *Cliente:* {nombre_cliente}
📞 *Teléfono:* {telefono}
--------------------------------
🍕 *PIZZAS ORDENADAS:* {resumen_pizzas_txt if resumen_pizzas_txt else ' (Ninguna)'}
--------------------------------
🥤 *Bebidas:* {texto_bebidas}
🍯 *Aderezos:* {texto_aderezos}
✍️ *Notas de Cocina:* {notas_pedido if notas_pedido else 'Ninguna'}
--------------------------------
💰 *TOTAL NETO A COBRAR:* ${total_general} MXN
"""

        # 3. Código mágico: Codificar el texto para que lo entienda un enlace web
        texto_codificado = urllib.parse.quote(mensaje_whatsapp)
        
        # 🚨 TU NÚMERO DE TELÉFONO AQUÍ 🚨
        # Reemplaza el 523300000000 por tu número real (incluyendo el código de país, ej. 52 para México)
        numero_pizzeria = "523342761208" 
        
        enlace_wa = f"https://wa.me/{numero_pizzeria}?text={texto_codificado}"

        # 4. Mostrar éxito en pantalla y dar el botón de redirección inmediata
        st.success(f"🎉 ¡Ticket generado con éxito, {nombre_cliente.upper()}!")
        
        # Botón dinámico que abre el chat de WhatsApp en una pestaña nueva
        st.link_button("📲 ABRIR WHATSAPP PARA CONFIRMAR TU PEDIDO", enlace_wa, use_container_width=True)

        # Dejar el resumen visual en pantalla por si acaso
        st.info(f"""
        **RESUMEN DEL TICKET GENERADO:**
        * **Cliente:** {nombre_cliente} ({telefono})
        ---
        **🍕 PIZZAS ORDENADAS:**{resumen_pizzas_txt if resumen_pizzas_txt else ' (Ninguna)'}
        ---
        * **🥤 Bebidas Seleccionadas:** {texto_bebidas}
        * **🍯 Aderezos Seleccionados:** {texto_aderezos}
        * **✍️ Notas Especiales:** {notas_pedido if notas_pedido else 'Ninguna'}
        ---
        * **💰 Total Neto a Cobrar:** ${total_general} MXN
        """)
